import requests

url1 = 'https://www.naver.com/'
url2 = 'https://news.naver.com/'    #get 요청이 거절되는 page

#현재 사용중인 브라우저 확인 → http://www.useragentstring.com/
#브라우저 종류 설정
requests_headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
     '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'),
}

try:
    res1 = requests.get(url1)
    print('header 미포함')
except:
    res1 = requests.get(url1, headers = requests_headers)
    print('header 포함')

print('status code :',res1.status_code)     #res1.ok 로도 확인 가능. 결과 : true or false)

try:
    res2 = requests.get(url2)
    print('header 미포함')
except:
    res2 = requests.get(url2, headers = requests_headers)
    print('header 포함')

print('status code :',res2.status_code)