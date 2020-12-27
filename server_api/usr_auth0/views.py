# from django.shortcuts import render

import json
from urllib.parse import urlencode

import django
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
# from django.http import HttpResponse
import jwt
from functools import wraps

from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """

    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    # print(token_scope)
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource.'})
            response.status_code = 403
            return response

        return decorated

    return require_scope


def auth0_login_check(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            user = request.user
        except Exception as e:
            return JsonResponse({'message':"No user in request!"})
        auth0user = user.social_auth.get(provider='auth0')
        if not user.is_authenticated or auth0user:
            return redirect('/login/auth0')

        return f(*args, **kwargs)

    return decorator


@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
# @login_required
# @permission_classes(['IsAuthenticated'])
def private(request):
    # return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }
    return JsonResponse({
        'userdata': json.dumps(userdata, indent=4)
    })

@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})

def logout(request):
    django.contrib.auth.logout(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)
