# gen token

from requests.auth import HTTPBasicAuth
import os
import requests
#from bs4 import Beautiful

data ='{"scopes":["repo"]}'

user = 'inishchith'
pw = 'Nks123456'
r = requests.post("https://api.github.com/authorizations",data=data,auth=HTTPBasicAuth(user, pw))
res = r.json()
if('token' in res.keys()):
	print(res['token'])
else:
	print(res['message'])