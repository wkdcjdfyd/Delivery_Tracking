import requests

url1:str = 'https://www.naver.com/'
url2:str = 'https://news.naver.com/'    #post 요청이 거절되는 page

requests_headers:dict = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
     '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'),
}

try:
    res1 = requests.post(url1)
    print('header 미포함')
except:
    res1 = requests.post(url1, headers = requests_headers)
    print('header 포함')

print('status code :',res1.status_code)

try:
    res2 = requests.post(url2)
    print('header 미포함')
except:
    res2 = requests.post(url2, headers = requests_headers)
    print('header 포함')

print('status code :',res2.status_code)