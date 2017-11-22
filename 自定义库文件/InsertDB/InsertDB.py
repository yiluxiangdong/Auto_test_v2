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
    def  InsertMysql(self,orderid,netType,type,names,posNo,provideType,result):
        names=str(names).decode('utf-8').encode('utf-8')
        createTime = time.strftime('%Y-%m-%d %H:%M:%S')
        self.cours.execute("insert into t_auto_test(orderId,netType,Types,shopName,posNo,provideType,result,createTime) values(%s,%s,%s,%s,%s,%s,%s,%s)", (orderid,netType,type,names,posNo,provideType,result,createTime))
        self.conn.commit()
    def  GetposNo(self,orderid):
        orderid = str(orderid)
        self.cours.execute("SELECT posNo FROM t_auto_test WHERE orderId=%s",orderid)
        return  self.cours.fetchone()[0]


    # def  updateType(self,orderid,type):
    #     type = str(type)
    #     if type=='rent':
    #       self.cours.execute("UPDATE  t_cm_order  SET  price=Null ,provideType=2,deposit=20000,buyway=NULL,packageId='02' WHERE orderId=%s", orderid)
    #
    #     elif type=='buy':
    #       self.cours.execute("UPDATE  t_cm_order  SET  price=29900,provideType=1,deposit=Null,buyway=1,packageId='01' WHERE orderId=%s;", orderid)
    #     else:
    #         pass
    #     self.conn.commit()
    def Getstatus(self,orderId):
        status = None
        orderId = str(orderId)
        self.cours.execute("SELECT orderStatus FROM t_cm_order WHERE orderId=%s", orderId)
        results = str(self.cours.fetchone()[0])
        if results=='2':
            status =  '入网失败'
        elif results=='4':
            status = '入网成功'
        return status

    def __del__(self):
        self.cours.close()
        self.conn.close()
if __name__ == '__main__':
    insertDB=InsertDB()
    # insertDB.GetposNo('1000000021025')
    # insertDB.Getstatus('1000000021019')
    insertDB.updateType('1000000021019','rent')










