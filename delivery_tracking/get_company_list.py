import requests
import json
#import sys

def Get_Company_List() -> dict:
    params: dict = {'t_key': ''}        #secret key
    res = requests.get('http://info.sweettracker.co.kr/api/v1/companylist',params=params)
    if res.status_code == 200:        #정상적으로 Company list를 가져왔을 경우
        data: dict = json.loads(res.text)
        return data
    else:
        data: dict = json.loads(res.text)
        print(data['msg'])            #가져오지 못했을 경우 Status 객체를 반환하므로 그 안의 msg를 출력
        #sys.exit()
        return None
    
if __name__ =="__main__":
    company: dict = Get_Company_List()
    print(company)