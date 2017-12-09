#!usr/bin/env python
#-*- coding:utf-8 _*-

from PIL import Image
import pytesseract
import pymysql
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class GetCode:
    def __init__(self):
        self.conn = pymysql.connect(host='172.20.21.176', port=3308, user='root', passwd='dev001', db='test',charset='utf8')
        self.cours = self.conn.cursor()
    def  getcode(self):
        im = Image.open(r'E:\abc\code.jpg')
        img_size = im.size
        x = 1039
        y = 600
        w = 70
        h = 38
        region = im.crop((x, y, x + w, y + h))
        region.save("./code_1.jpg")
        qqs = Image.open('code_1.jpg')
        codes = pytesseract.image_to_string(qqs).strip()
        print codes
        return str(codes)

    def  InsertMysql(self,orderid,netType,type,names,posNo,provideType,result,SettleType,communicationsFee,addNew,FeeType):
        names=str(names).decode('utf-8').encode('utf-8')
        createTime = time.strftime('%Y-%m-%d %H:%M:%S')
        FeeType = str(FeeType)
        if FeeType=='月付':
            FeeTypes='月付通讯费5元'
        elif FeeType=='年付':
            FeeTypes = '年付通讯费180元'
        insertSQL="insert into t_auto_test(orderId,netType,Types,shopName,posNo,provideType,result,SettleType,communicationsFee,addNew,FeeType,createTime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cours.execute(insertSQL, (orderid,netType,type,names,posNo,provideType,result,SettleType,communicationsFee,addNew,FeeTypes,createTime))
        self.conn.commit()
    def  GetposNo(self,orderid):
        orderid = str(orderid)
        self.cours.execute("SELECT posNo FROM t_auto_test WHERE orderId=%s  ORDER BY  createTime DESC", orderid)
        return  self.cours.fetchone()[0]
    def  Getstatus(self,orderId):
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
    # picPath = r'E:\abc\code.jpg'
    getCode=GetCode()
    getCode.getcode()

