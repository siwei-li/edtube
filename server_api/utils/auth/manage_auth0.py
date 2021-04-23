# manage_auth0.py created by sylvi at 2020/12/31 10:12 AM
import json, requests
from requests.exceptions import RequestException, HTTPError, URLRequired

# Configuration Values
import environ
env = environ.Env()
environ.Env.read_env()

domain = 'edtube.us.auth0.com'
audience = f'https://{domain}/api/v2/'
client_id = env.str('CLIENT_ID')
client_secret = env.str('CLIENT_SECRET')
grant_type = "client_credentials" # OAuth 2.0 flow to use
base_url = f"https://{domain}"

def get_management_access_token():
    # Get an Access Token from Auth0

    payload = {
        'grant_type': grant_type,
        'client_id': client_id,
        'client_secret': client_secret,
        'audience': audience
    }
    response = requests.post(f'{base_url}/oauth/token', data=payload)
    oauth = response.json()
    access_token = oauth.get('access_token')

    return access_token


def call_auth0_management(url, method, data=None):

  access_token = get_management_access_token()

  # Add the token to the Authorization header of the request
  headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
  }

  try:
    # res = requests.get(f'{base_url}/api/v2/{action}', headers=headers)
    method_to_call = getattr(requests,method)
    res = method_to_call(f'{base_url}/api/v2/{url}', data, headers=headers)
    return res.json()
  except HTTPError as e:
    return f'HTTPError: {str(e.code)} {str(e.reason)}'
  except URLRequired as e:
    return f'URLRequired: {str(e.reason)}'
  except RequestException as e:
    return f'RequestException: {e}'
  except Exception as e:
    return f'Generic Exception: {e}'

if __name__ == '__main__':
  # print(call_auth0_management('users','get'))
  print(call_auth0_management('users/auth0%7C5fe2cffe08284b006bb4ff09','patch','{"nickname":"lol"}'))