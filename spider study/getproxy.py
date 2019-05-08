import requests,json
import re
import random

#获取免费代理存入ip.json
def setIps(index=0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    #https \ http \ 国普 \ 高匿
    url=['https://www.xicidaili.com/wn/','https://www.xicidaili.com/wt/','https://www.xicidaili.com/nt/','https://www.xicidaili.com/nn/']
    r = requests.get(url[index], headers=headers)
    text = re.search('ip_list.*?</table>',r.text,re.S).group()
    text = re.sub('ip_list(.|\n)*?<\/tr>','',text,re.S)
    pattern = re.compile('(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})', re.S)
    pattern2 = re.compile('<td>(\d+)</td>', re.S)
    pattern3 = re.compile('<td>(http|HTTP|HTTPS|https)</td>', re.S)
    ips = re.findall(pattern, text)
    ports = re.findall(pattern2, text)
    xys = re.findall(pattern3, text)
    res = []
    for i in range(len(xys)):
        res.append({
            'type':xys[i].lower(),
            'url':xys[i].lower()+"://"+ips[i]+":"+ports[i]
        })
    with open('ip.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(res, indent=2, ensure_ascii=False))
        
#从ip.json读取所有代理
def getIps():
    with open('ip.json', 'r') as file:
        str = file.read()
        data = json.loads(str)
        return data
#随机取得一个代理
def getIp(ips=[]):
    if ips:
        return ips[random.randint(0, len(ips)-1)]
    else:    
        with open('ip.json', 'r') as file:
            ips = json.loads(file.read())
            return ips[random.randint(0, len(ips)-1)]

