from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener,ProxyHandler,HTTPCookieProcessor
from urllib.error import URLError
import http.cookiejar
import re
from bs4 import BeautifulSoup
from getproxy import getIp,getIps,setIps


# setIps(1)
ips=getIps()
def getHtml(url):
    ip = getIp(ips)
    proxy_handler = ProxyHandler({
        ip['type']:ip['url']
    })

    opener = build_opener(proxy_handler)
    try:
        result = opener.open(url)
        html = result.read().decode('utf-8')
        
        soup = BeautifulSoup(html, 'lxml')
        arr=[]
        for div in soup.find_all(class_='content__list--item--main'):
            title = div.find(class_='content__list--item--title').find(name='a').string.strip()
            des = div.find(class_='content__list--item--des')
            
            size = des.find(text=re.compile('\d*㎡')).strip()
            price = div.find(class_='content__list--item-price').find('em').string.strip()
            time = div.find(text=re.compile('content__list--item--time.*?>(.*?)</p>',re.S))
            time = re.search('.*?>(.*?)</p>',div.find(class_='content__list--item--time').prettify(),re.S).group(1).strip()
            tags = re.findall('<i.*?>[\s\n]*(.*?)[\s\n]*</i>',div.find(class_='content__list--item--bottom').prettify(),re.S)
            huxing = re.search('</i>.*?</i>.*?</i>(.*?)<',des.prettify(),re.S).group(1).strip()
            floor = re.findall('\S*[层室]',div.find(name='span',class_="hide").prettify(),re.S)
            floor_type = floor[0]
            floor_num = floor[1][1:-1]
            shen = "北京市"
            qu = re.search('<a.*?>(.*?)</a>',des.prettify(),re.S).group(1).strip()
            qu2 = re.search('<a.*?</a>.*?<a.*?>(.*?)</a>',des.prettify(),re.S).group(1).strip()
            if re.search('整租',title,re.S):
                xiangxidizhi = re.search('整租[ · ，]*(\S*)',title,re.S).group(1).strip()
                zhengzu = '整租'
            else:
                xiangxidizhi = re.search('\S*',title,re.S).group().strip()
                zhengzu = ""
            chaoxiang = re.search('</i>.*?</i>(.*?)<i>',des.prettify(),re.S).group(1).strip()
            arr.append({
                'title':title,
                'size':size,
                'price':price,
                'time':time,
                'tags':tags,
                'huxing':huxing,
                'floor':floor_num,
                'floor_type':floor_type,
                'chaoxiang':chaoxiang,
                'shen':shen,
                'qu':qu,
                'qu2':qu2,
                'xiangxidizhi':xiangxidizhi,
                'zhengzu':zhengzu
            })
        return arr
    except URLError as e:
        print(e.reason)
        


##x需要直接登录
## username = 'username'
## password = 'password'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)

##设置代理
# ip = getip()
# proxy_handler = ProxyHandler({
#     ip['type']:ip['url']
# })

## #设置cookie
## cookie = http.cookiejar.CookieJar()
## handler = HTTPCookieProcessor(cookie)

## ##
## opener = build_opener(auth_handler,proxy_handler,handler)
# opener = build_opener(proxy_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)



# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
# ip = getip()
# proxy_handler = ProxyHandler({
#     ip['type']:ip['url']
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

