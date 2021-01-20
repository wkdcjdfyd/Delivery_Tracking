import requests

url:str  = 'https://news.naver.com/main/list.nhn?'

requests_headers:dict = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
     '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'),
}

requests_data:dict = {      # post 사용시에는 params 대신 data
    'sid1' : '104',
    'sid2' : '231',
    'date' : '20210120',
    'page' : '1'
}

res = requests.post(url, headers = requests_headers, data = requests_data)

print(res)