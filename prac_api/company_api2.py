import requests
import json

base_url: str = 'http://info.sweettracker.co.kr'
api_url: str = '/api/v1/companylist'

api_params: dict = {
    't_key' : ''  #secret key
}

res = requests.get(base_url+api_url, params = api_params)
data = json.loads(res.text)

print(type(res.text))
print(res.text)

print('\n')

print(type(data))
print(data)

for x in data['Company']:
   print(x)