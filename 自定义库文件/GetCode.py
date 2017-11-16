#!usr/bin/env python
#-*- coding:utf-8 _*-
import random
class GetCode:
    ROBOT_LIBRARY_SCOPE = 'Global'
    def __init__(self):
        pass

    def get_num(self):
        numbers = random.randint(999,10000)
        print numbers
        return numbers


if __name__ == '__main__':
    getcode = GetCode()
    getcode.get_num()
