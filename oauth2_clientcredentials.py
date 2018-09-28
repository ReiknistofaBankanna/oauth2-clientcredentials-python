import sys
import urllib.request
import urllib.parse
import json
import jwt

if (len(sys.argv) != 5):
    print('Usage... adfsUrl clientId clientSecret resource')
    sys.exit(2)

url = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]
resource = sys.argv[4]


postdata = { 'client_id': client_id, 'client_secret': client_secret, 'grant_type' : 'client_credentials', 'resource': resource }
data = bytes( urllib.parse.urlencode( postdata ).encode() )

f = urllib.request.urlopen(url, data)

response = f.read().decode('utf-8')
print(response)
    