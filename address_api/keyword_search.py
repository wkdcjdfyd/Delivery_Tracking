import requests
import json

BASE_URL: str = 'https://dapi.kakao.com/v2/local/search'
KEYWORD_SEARCH: str  = '/keyword.json?'

headers: dict = {
    'Authorization': ''  #secret key
}

keyword_params: dict = {
    'analyze_type': 'similar',
    'query': ''
}

keyword_res = requests.get(BASE_URL+KEYWORD_SEARCH, headers = headers, params = keyword_params)
keyword_data: dict = json.loads(keyword_res.text)

print(keyword_data, '\n')