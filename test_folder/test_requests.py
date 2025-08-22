import requests

url = 'https://www.whois.com/whois/'

r = requests.get(url)


if r.status_code==200:
    # page works, check if text or json response
    if r.headers['Content-Type'] == 'text/html; charset=UTF-8':
        print(r.text)
    
    
else:
    print('no website')


