#!usr/bin/env python
#-*- coding:utf-8 _*-
import pymysql
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class InsertDB:
    def __init__(self):
        self.conn = pymysql.connect(host='172.20.21.176', port=3308, user='root', passwd='dev001', db='test', charset='utf8')
        self.cours = self.conn.cursor()
    def  InsertMysql(self,orderid,netType,type,names,posNo):
        names=str(names).decode('utf-8').encode('utf-8')
        createTime = time.strftime('%Y-%m-%d %H:%M:%S')
        self.cours.execute("insert into t_auto_test(orderId,netType,Types,shopName,posNo,createTime) values(%s,%s,%s,%s,%s,%s)", (orderid,netType,type,names,posNo,createTime))
    def  GetposNo(self,orderid):
        self.cours.execute("SELECT posNo FROM t_auto_test WHERE orderId=%s",orderid)
        return  self.cours.fetchone()[0]

    def __del__(self):
        self.conn.commit()
        self.cours.close()
        self.conn.close()
if __name__ == '__main__':
    insertDB=InsertDB()
    insertDB.GetposNo('1000000011817')








