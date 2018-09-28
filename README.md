oauth2-clientcredentials-python
==================================

This sample calls a oAuth2 Authorization Server to get a JWT token using the client credentials flow.

## How To Run This Sample

### To run this sample you will need:
- Python 3

### Python packages:
- request
- jwt
- json

### Usage:
Usage... adfsUrl clientId clientSecret resource

Example:
```
python oauth2_clientcredentials.py https://adfs.test.rb.is/adfs/oauth2/token bc23c39e-5303-488d-920c-acb6af33455 mysecret urn:rb.api
```
