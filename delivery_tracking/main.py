import requests
import json
import sys
from get_company_list import Get_Company_List
from get_location import Get_Location
from tracking import Tracking

if __name__ =="__main__":
    invoice: str = input('송장번호 : ')
    com_name: str = input('택배사 이름 : ')

    data: list = Tracking(invoice, com_name)       #date는 tracking_details list\

    for x in data:
        if not x['telno']:
            print('전화번호가 없을 때')
            print(com_name+x['where'])
            location: tuple = Get_Location(com_name+x['where'])
            if not location: #택배사 이름 + 경유지 이름으로 검색결과가 없을 경우
                print('위치를 찾지 못했습니다')
        else:
            if '010' in x['telno']:
                print('전화번호에 010 포함일 때')
                print(com_name+x['where'])
                location: tuple = Get_Location(com_name+x['where'])
            else:
                print('전화번호로 검색')
                print(x['telno'])
                location: tuple = Get_Location(x['telno'])
                if not location:    #전화번호로 위치를 찾지 못했을 경우
                    print('전화번호로 검색을 실패해서 택배사 이름 + 경유지 이름로 검색')
                    print(com_name+x['where'])
                    location: tuple = Get_Location(com_name+x['where'])
        print(location)
        print('\n')
