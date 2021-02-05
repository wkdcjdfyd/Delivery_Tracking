from get_company_list import get_company_list, GetCompanyListError
from get_tracking_details import get_tracking_details, GetTrackingDetailsError
from get_location import get_location, GetLocationError, NoSearchResultError
from typing import List, Tuple

if __name__ =="__main__":
    invoice: str = input('송장번호 : ')
    com_name: str = input('택배사 이름 : ')

    try:
        data: List[str] = get_tracking_details(invoice, com_name)       #data는 tracking details list
    except GetCompanyListError as e:
        print(e)
    except GetTrackingDetailsError as e:
        print(e)


    for x in data:
        if not x['telno']:
            try:
                location: Tuple[str, str] = get_location(com_name + x['where'])  #전화번호가 없어서 택배사 이름 + 경유지 이름로 검색
            except GetLocationError as e:
                print(e)
            except NoSearchResultError as e:
                print(e)
        else:
            if '010' in x['telno']:               #전화번호가 있지만 핸드폰 번호일 경우
                try:
                    location: Tuple[str, str] = get_location(com_name + x['where'])
                except GetLocationError as e:
                    print(e)
                except NoSearchResultError as e:
                    print(e)
            else:
                try:
                    location: Tuple[str, str] = get_location(x['telno'])
                except GetLocationError as e:
                    print(e)
                except NoSearchResultError as e:
                    try:
                        location: Tuple[str, str] = get_location(com_name + x['where'])
                    except GetLocationError as e:
                        print(e)
                    except NoSearchResultError as e:
                        print(e)
        print(location)
        print('\n')
