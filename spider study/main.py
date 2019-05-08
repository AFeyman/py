import datetime
from myhtml import getHtml
from db import Db

db = Db()
start_time = datetime.datetime.now()

def run(page):
    global start_time,datetime
    page=page+1
    quer = 'pg'+str(page) if page>1 else ''
    url="https://bj.lianjia.com/zufang/dongcheng/"+quer
    arr = getHtml(url)
    if len(arr)==0:
        db.close()
        print('全爬完，总耗时：',(datetime.datetime.now()-start_time).seconds,'秒')
        return
    
    keys=[]
    for i in arr[0]:
        keys.append(i)
    value=[]
    for i in arr:
        tstr = ''
        for idx in keys:
            if isinstance(i[idx],str):
                tstr +='"'+ i[idx]+'",'
            else:
                tstr+='"'+','.join(i[idx])+'",'
        value.append(tstr[:-1])
        # break
    db.insert('beijing',keys,value)
    
    print(page,'页， ',len(arr),'条数据','over,计时',(datetime.datetime.now()-start_time).seconds,'秒')
    run(page)
run(0)