# from django.shortcuts import render

from django.http import JsonResponse
# from django.http import HttpResponse

import jwt
from functools import wraps

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from .models import Profile
from usr_auth0.serializers import ProfileSerializer, NicknameSerializer
from utils.auth.manage_auth0 import call_auth0_management

# import base64
#
# from xmlrpc.client import ServerProxy, Fault
# from hashlib import md5
#
# class GravatarXMLRPC(object):
#     API_URI = 'https://secure.gravatar.com/xmlrpc?user={0}'
#
#     def __init__(self, request, password=''):
#         self.request = request
#         self.password = password
#         self.email = sanitize_email(request.user.email)
#         self.email_hash = md5_hash(self.email)
#         self._server = ServerProxy(
#             self.API_URI.format(self.email_hash))
#
#     def saveData(self, image):
#         """ Save binary image data as a userimage for this account """
#         # params = { 'data': base64_encode(image.read()), 'rating': 0, }
#         # return self._call('saveData', params)
#         return self._call('saveData', image)
#         # return self.useUserimage(image)
#
#     def _call(self, method, params={}):
#         """ Call a method from the API, gets 'grav.' prepended to it. """
#         args = {'password': self.password, }
#         args.update(params)
#
#         try:
#             return getattr(self._server, 'grav.' + method, None)(args)
#         except Fault as error:
#             error_msg = "Server error: {1} (error code: {0})"
#             print(error_msg.format(error.faultCode, error.faultString))
#
#
# def base64_encode(obj):
#     return base64.b64encode(obj)
#
#
# def sanitize_email(email):
#     return email.lower().strip()
#
#
# def md5_hash(string):
#     return md5(string.encode('utf-8')).hexdigest()


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
    """Determines if the required permission is present in the Access Token
    Args:
        required_permission (str): The permission required to access the resource
    """

    def require_permission(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("permission"):
                token_permissions = decoded["permission"]
                for token_permission in token_permissions:
                    if token_permission == required_permission:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response

        return decorated

    return require_permission


@swagger_auto_schema(methods=['PUT'], request_body=ProfileSerializer, tags=["profile"], \
                     responses={
                         200: openapi.Response('Profile updated successfully!', ProfileSerializer), }
                     )
@api_view(['PUT'])
def update_profile(request):
    '''
    Update user profile information.
    '''
    user_id = request.user.id
    profile = Profile.objects.get(auth0_user_id=user_id)

    profile_data = JSONParser().parse(request)
    profile_serializer = ProfileSerializer(data=profile_data)

    if profile_serializer.is_valid():
        profile.gender = profile_serializer.data['gender']
        profile.bio = profile_serializer.data['bio']
        profile.birth_date = profile_serializer.data['birth_date']
        profile.save()

        return JsonResponse({"profile": profile_serializer.data})
    return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['PATCH'], request_body=NicknameSerializer, tags=["profile"],\
                     responses={
                         200: openapi.Response('Nickname updated successfully!', NicknameSerializer),
                         400: openapi.Response("Error: Nickname data format error"),
                         500: openapi.Response("Error: Internal server error"),
                     })
@api_view(['PATCH'])
def update_nickname(request):
    user_id = request.user.username.replace('.', '|')
    request_data = JSONParser().parse(request)

    nickname_serializer = NicknameSerializer(data=request_data)

    if nickname_serializer.is_valid():
        # res = call_auth0_management(f'users/{user_id}', 'patch', '{"nickname":"lol"}')
        data = JSONRenderer().render(nickname_serializer.data)
        res = call_auth0_management(f'users/{user_id}', 'patch', data)
        print("Auth0 API error:",res,"================")
        # TODO
        if res['statusCode']!=200:
            return JsonResponse({"Error": "Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse(res)
    return JsonResponse({"error": nickname_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PATCH'])
# def profile_pic(request):
#     request_data = JSONParser().parse(request)
#     print(request_data['file'])
#
#     GravatarXMLRPC(request).saveData(request_data['file'])
#
#     return JsonResponse({"message":"Image successfully uploaded:"})


# Testing Restful API =======================================================
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def public(request):
#     return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})
#
#
# @api_view(['GET'])
# def private(request):
#     user_id = request.user.username
#     return JsonResponse({'message': f'Hello, {user_id}! You need to be authenticated to see this.'})
#
#
# @api_view(['GET'])
# @requires_permission('read:messages')
# # @requires_scope('read:messages')
# def private_scoped(request):
#     return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})
