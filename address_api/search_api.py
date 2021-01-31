import requests
import json

BASE_URL: str = 'https://dapi.kakao.com/v2/local/search'
KEYWORD_SEARCH: str  = '/keyword.json?'
ADDRESS_SEARCH: str  = '/address.json?'

headers: dict = {
    'Authorization': ''  #secret key
}

keyword_params: dict = {
    'analyze_type': 'similar',
    'query': ''
}

address_params: dict = {
    'analyze_type': 'similar',
    'query': ''
}

keyword_params['query'] = input('전화번호 : ')

keyword_res = requests.get(BASE_URL+KEYWORD_SEARCH, headers = headers, params = keyword_params)
keyword_data: dict = json.loads(keyword_res.text)

print(keyword_data, '\n')

address: str = keyword_data['documents'][0]['address_name']
address_params['query'] = address

print(address, '\n')

address_res = requests.get(BASE_URL+ADDRESS_SEARCH, headers = headers, params = address_params)
address_data: dict = json.loads(address_res.text)

print(address_data, '\n')

latitude: str = address_data['documents'][0]['y']
longitude: str = address_data['documents'][0]['x']

print(latitude, longitude)