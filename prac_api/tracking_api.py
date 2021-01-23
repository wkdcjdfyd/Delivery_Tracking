import requests

base_url:str = 'http://info.sweettracker.co.kr'
api_url:str = '/api/v1/trackingInfo'

api_params:dict = {
    't_key' : '',       #secret key
    't_code' : '',      #택배사 코드
    't_invoice' : ''    #운송장 번호
}

res = requests.get(base_url+api_url, params = api_params)

print(res)
print(res.text)