from get_company_list import Get_Company_List
import json
import requests
import sys

def Tracking(invoice: str, com_name: str) -> list:      #invoice = 송장번호, com_name = 택배사 이름
    params: dict = {'t_key': ''}                        #secret key
    params['t_invoice'] = invoice

    com_list = Get_Company_List()

    for x in com_list['Company']:
        if x['Name'] == com_name:
            params['t_code'] = x['Code']

    res = requests.get('http://info.sweettracker.co.kr/api/v1/trackingInfo', params = params)

    if res.status_code == 200:        #정상적으로 정보를 가져왔을 경우
        data: dict = json.loads(res.text)
        return data['trackingDetails']
    else:
        data: dict = json.loads(res.text)
        print(data['msg'])            #가져오지 못했을 경우 Status 객체를 반환하므로 그 안의 msg를 출력
        sys.exit()
        return None

if __name__ =="__main__":
    invoice: str = input('송장번호 : ')
    com_name: str = input('택배사 이름 : ')

    data: list = Tracking(invoice, com_name)

    print(data)