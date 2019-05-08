import pymysql

class Db:
    def __init__(self,host='localhost',usr='root',psd='123',base='链家'):
        # self.db = pymysql.connect('localhost',"root","123","链家")
        self.db = pymysql.connect(host,usr,psd,base)
        self.cursor = self.db.cursor()
    def insert(self,table,key,value):
        valuestr=''
        for i in value:
            valuestr+='('+i+'),'
        sql = 'INSERT INTO '+table+'('+','.join(key)+')VALUES '+valuestr[:-1]
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    def query(self,table,key='*',where=''):
        sql = "SELECT "+key+" FROM "+table+' '+where 
            #    WHERE INCOME > %s" % (1000)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            # print(results)
            # arr=[]
            # for row in results:
            #     arr.append({'FIRST_NAME':row[0],'LAST_NAME':row[1]})
            return results
        except:
            print ("Error: unable to fetch data")
    def close(self):
        self.db.close()

# db = Db()
# db.insert('EMPLOYEE','FIRST_NAME,LAST_NAME',['1,1','2,2','3,3'])
# db.query('EMPLOYEE','*')
# db.close()

    
    
    
    
# # 打开数据库连接
# db = pymysql.connect("localhost","root","123","链家" )

# cursor = db.cursor()
 
# # SQL 插入语句
# sql = 'INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME)
#          VALUES ('Mac', 'Mohan')'
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()
 
# # 关闭数据库连接
# db.close()