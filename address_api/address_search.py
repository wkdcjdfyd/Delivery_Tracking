import requests
import json

BASE_URL: str = 'https://dapi.kakao.com/v2/local/search'
ADDRESS_SEARCH: str  = '/address.json?'

headers: dict = {
    'Authorization': ''  #secret key
}

address_params: dict = {
    'analyze_type': 'similar',
    'query': ''
}

address_res = requests.get(BASE_URL+ADDRESS_SEARCH, headers = headers, params = address_params)
address_data: dict = json.loads(address_res.text)

print(address_data, '\n')