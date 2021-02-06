from get_company_list import get_company_list, GetCompanyListError
from get_tracking_details import get_tracking_details, GetTrackingDetailsError
from get_location import get_location, GetLocationError, NoSearchResultError
from typing import List, Tuple
import json

if __name__ == "__main__":
    invoice: str = input('송장번호 : ')
    com_name: str = input('택배사 이름 : ')

    info: dict = {'Locations': []}

    try:
        data: List[str] = get_tracking_details(
            invoice, com_name)  # data는 tracking details list
    except GetCompanyListError as e:
        print(e)
    except GetTrackingDetailsError as e:
        print(e)

    step: int = 1

    for x in data:
        if not x['telno']:
            try:
                # 전화번호가 없어서 택배사 이름 + 경유지 이름로 검색
                location: dict = get_location(com_name + x['where'])
                location['step'] = step
                step += 1
                info['Locations'].append(location)
            except GetLocationError as e:
                print(e)
            except NoSearchResultError as e:
                print(e)
        else:
            if '010' in x['telno']:  # 전화번호가 있지만 핸드폰 번호일 경우
                try:
                    location: dict = get_location(com_name + x['where'])
                    location['step'] = step
                    step += 1
                    info['Locations'].append(location)
                except GetLocationError as e:
                    print(e)
                except NoSearchResultError as e:
                    print(e)
            else:
                try:
                    location: dict = get_location(x['telno'])
                    location['step'] = step
                    step += 1
                    info['Locations'].append(location)
                except GetLocationError as e:
                    print(e)
                except NoSearchResultError as e:
                    try:
                        location: dict = get_location(com_name + x['where'])
                        location['step'] = step
                        step += 1
                        info['Locations'].append(location)
                    except GetLocationError as e:
                        print(e)
                    except NoSearchResultError as e:
                        print(e)

    with open('info.json', 'w', encoding='utf-8') as make_file:
        json.dump(info, make_file, ensure_ascii=False, indent='\t')
