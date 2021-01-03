# from django.shortcuts import render

from django.http import JsonResponse
# from django.http import HttpResponse

import jwt
from functools import wraps

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from usr_auth0.serializers import ProfileSerializer, NicknameSerializer
from utils.auth.manage_auth0 import call_auth0_management


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
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response

        return decorated

    return require_scope


def requires_permission(required_permission):
    def require_permission(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("permissions"):
                token_permissions = decoded["permission"]
                for token_permission in token_permissions:
                    if token_permission == required_permission:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response

        return decorated

    return required_permission


@api_view(['PUT'])
def update_profile(request):
    # username = request.user.username
    user = request.user

    profile_data = JSONParser().parse(request)
    profile_serializer = ProfileSerializer(user.profile, data=profile_data)
    if profile_serializer.is_valid():
        profile_serializer.save()

        return JsonResponse({"user": user, "Profile": profile_serializer.data})
    return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    # user.save()


@api_view(['PATCH'])
def update_nickname(request):
    user_id = request.user.username.replace('.', '|')
    request_data = JSONParser().parse(request)

    nickname_serializer = NicknameSerializer(data=request_data)
    if nickname_serializer.is_valid():
        call_auth0_management(f'users/{user_id}', 'patch', nickname_serializer.validated_data)
        return JsonResponse({"user": user_id, "nickname": nickname_serializer.validated_data})
    return JsonResponse(nickname_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def profile_pic(requests):

    return JsonResponse({"message":"Image successfully uploaded."})

# Testing Restful API =======================================================
@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
def private(request):
    user_id = request.user.username
    return JsonResponse({'message': f'Hello, {user_id}! You need to be authenticated to see this.'})


@api_view(['GET'])
@requires_permission('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})
