import requests
import json

BASE_URL: str = 'http://info.sweettracker.co.kr'
COMPANY_URL: str = '/api/v1/companylist'
TRACKING_URL: str = '/api/v1/trackingInfo'
HEAD: str = '       배송시간        현재위치       배송상태'
TAIL: str = '-------------------------------------------------'

api_params: dict = {
    't_key' : '',       #secret key
}

def get_t_code(name: str, company: dict) -> str:
    for x in company['Company']:
        if x['Name'] == name:
            return x['Code']

def get_company_list() -> dict:
    res = requests.get(BASE_URL+COMPANY_URL, params = api_params)
    data: dict = json.loads(res.text)
    return data

def tracking() -> None:
    res = requests.get(BASE_URL+TRACKING_URL, params = api_params)
    data: dict = json.loads(res.text)
    print(HEAD)
    print(TAIL)
    for x in reversed(data['trackingDetails']):
        print(x['timeString'], x['where'], x['kind'].replace('\n', ' '))
    print(TAIL)

if __name__ =="__main__":
    api_params['t_invoice'] = input('송장번호 : ')
    name: str = input('택배사이름 : ')
    print(TAIL)

    company_list: dict = get_company_list()

    api_params['t_code'] = get_t_code(name, company_list)

    tracking()