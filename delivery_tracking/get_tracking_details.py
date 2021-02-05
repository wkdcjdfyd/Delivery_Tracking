from get_company_list import get_company_list, GetCompanyListError
from typing import List
import json
import requests

class GetTrackingDetailsError(Exception):
    pass

def get_tracking_details(invoice: str, com_name: str) -> List[str]: # invoice = 송장번호, com_name = 택배사 이름
    params: dict = {'t_key': ''}  # secret key
    params['t_invoice'] = invoice

    com_list: List[str] = get_company_list()

    for x in com_list:
        if x['Name'] == com_name:
            params['t_code'] = x['Code']

    res = requests.get('http://info.sweettracker.co.kr/api/v1/trackingInfo', params=params)
    if res.status_code == 200:  # 정상적으로 정보를 가져왔을 경우
        data: dict = json.loads(res.text)
        return data['trackingDetails']
    else:
        data: dict = json.loads(res.text)
        raise GetTrackingDetailsError(data['msg'])    # 가져오지 못했을 경우 Status 객체를 반환하므로 그 안의 msg를 출력


if __name__ == "__main__":
    invoice: str = input('송장번호 : ')
    com_name: str = input('택배사 이름 : ')

    try:
        data: List[str] = get_tracking_details(invoice, com_name)
        print(data)
    except GetCompanyListError as e:
        print(e)
    except GetTrackingDetailsError as e:
        print(e)
