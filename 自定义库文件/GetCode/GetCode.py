#!usr/bin/env python
#-*- coding:utf-8 _*-

from PIL import Image
import pytesseract
class GetCode:
    def  getcode(self):
        im = Image.open(r'E:\abc\code.jpg')
        img_size = im.size
        x = 1039
        y = 617
        w = 70
        h = 38
        region = im.crop((x, y, x + w, y + h))
        region.save("./code_1.jpg")
        qqs = Image.open('code_1.jpg')
        codes = pytesseract.image_to_string(qqs).strip()
        print codes
        return str(codes)

if __name__ == '__main__':
    picPath = r'E:\abc\code.jpg'
    getCode=GetCode()
    getCode.getcode()
