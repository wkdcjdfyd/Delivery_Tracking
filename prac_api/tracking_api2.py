import requests
import json

base_url: str = 'http://info.sweettracker.co.kr'
company_url: str = '/api/v1/companylist'
tracking_url: str = '/api/v1/trackingInfo'

api_params: dict = {
    't_key' : '',       #secret key
}

def get_t_code(name: str, company: dict) -> str:
    for x in range(len(company['Company'])):
        if company['Company'][x]['Name'] == name:
            return company['Company'][x]['Code']

def get_company_list() -> dict:
    res = requests.get(base_url+company_url, params = api_params)
    data: dict = json.loads(res.text)
    return data

if __name__ =="__main__":
    api_params['t_invoice'] = input('송장번호 : ')
    name:str = input('택배사이름 : ')

    company_list: dict = get_company_list()

    api_params['t_code'] = get_t_code(name, company_list)

    res = requests.get(base_url+tracking_url, params = api_params)

    print(res)
    print(res.text)