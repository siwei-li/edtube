HEADER:ALGORITHM & TOKEN TYPE

```
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "aFqoKqq_TEPbLJ_DtyUHL"
}
```

PAYLOAD:DATA

```
{
  "iss": "https://edtube.us.auth0.com/",
  "sub": "auth0|5fe2cffe08284b006bb4ff09",
  "aud": [
    "https://edtube",
    "https://edtube.us.auth0.com/userinfo"
  ],
  "iat": 1609075811,
  "exp": 1609162211,
  "azp": "hI93iPGM9x4wnbeRxSn0CpoiOGBEasSq",
  "scope": "openid profile email offline_access",
  "permissions": [
    "read:messages"
  ]
}
```

VERIFY SIGNATURE

```
RSASHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  ,
  
)
```