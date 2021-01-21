import requests

url:str  = 'https://news.naver.com/main/list.nhn?'

requests_headers:dict = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
     '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'),
}

requests_params:dict = {      # 네이버뉴스 > 세계 > 아사아/호주 > 날짜 > 1페이지
    'sid1' : '104',           # tuple 도 사용가능
    'sid2' : '231',
    'date' : '20210120',
    'page' : '1'
}

res = requests.get(url, headers = requests_headers, params = requests_params)

print(res)