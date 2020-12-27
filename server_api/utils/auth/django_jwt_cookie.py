# django_jwt_cookie.py created by sylvi at 2020/12/26 10:22 PM

"""
This file contains a custom Django SessionStore and middleware for using a JWT
token inside the Django session cookie. The token plays well with Django Rest
Framework and it's JWT library: django-rest-framework-jwt.
Usage:
- add this file to settings.py SESSION_ENGINE
- add jwt_session_middleware to settings.py MIDDLEWARE
- set JWT_USER_FIELDS (and configure django-rest-framework-jwt's
  JWT_PAYLOAD_GET_USERNAME_HANDLER accordingly)
"""
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.sessions.backends.signed_cookies import SessionStore

from rest_framework_jwt.settings import api_settings


JWT_USER_FIELDS = ['email', 'slug']  # OR: load these from settings


class SessionStore(SessionStore):

    def load(self):
        """
        We load the data from the key itself instead of fetching from
        some external data store. Opposite of _get_session_key(),
        raises BadSignature if signature fails.
        """
        try:
            return api_settings.JWT_DECODE_HANDLER(self.session_key)
        except Exception:
            # BadSignature, ValueError, or unpickling exceptions. If any of
            # these happen, reset the session.
            self.create()
        return {}

    def _get_session_key(self):
        """
        Most session backends don't need to override this method, but we do,
        because instead of generating a random string, we want to actually
        generate a JWT Token with DRF-JWT.
        """
        session_cache = getattr(self, '_session_cache', {})
        return api_settings.JWT_ENCODE_HANDLER({
            **session_cache,
            'exp': datetime.utcnow() + timedelta(seconds=settings.SESSION_COOKIE_AGE)
            # any other JWT fields like 'iss' etc. could be added here...
            # see: https://github.com/GetBlimp/django-rest-framework-jwt/blob/master/rest_framework_jwt/utils.py#L11
        })


def jwt_session_middleware(get_response):
    """
    Middleware that adds JWT_USER_FIELDS into the session for all logged in Users.
    """

    def middleware(request):
        response = get_response(request)

        if request.user.is_anonymous:
            return response

        for field in JWT_USER_FIELDS:
            if field not in request.session:
                request.session[field] = getattr(request.user, field)

        # update 'exp' here if about the expire ?

        return response

    return middleware