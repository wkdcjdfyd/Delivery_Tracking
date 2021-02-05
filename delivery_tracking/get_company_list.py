from typing import List
import requests
import json

class GetCompanyListError(Exception):
    pass

def get_company_list() -> List[str]:
    params: dict = {'t_key': ''}        #secret key
    res = requests.get('http://info.sweettracker.co.kr/api/v1/companylist',params=params)
    if res.status_code == 200:        #정상적으로 Company list를 가져왔을 경우
        data: dict = json.loads(res.text)
        return data['Company']
    else:
        data: dict = json.loads(res.text)
        raise GetCompanyListError(data['msg'])  #가져오지 못했을 경우 Status 객체를 반환하므로 그 안의 msg를 출력
    
if __name__ =="__main__":
    try:
        company: List[str] = get_company_list()
        print(company)
    except GetCompanyListError as e:
        print(e)