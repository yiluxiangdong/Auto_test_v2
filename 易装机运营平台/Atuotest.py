#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:liuxiaobing 
@time: 2017/11/15 
"""
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = raw_input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
#
#
# printBoard(theBoard)
###############################################
# print 'hello'.startswith('he')
# print 'hello'.startswith('e')
# print 'hello'.endswith('o')
# print 'hello'.endswith('h')
# print 'hello'.rjust(10)+'||||'
# print 'hello'.rjust(20)+'||||'
# print 'hello'.ljust(10)+'||||'
# print 'hello'.ljust(20)+'||||'
# print 'hello'.center(20)+'||||'
###############################################
# import pyperclip
# pyperclip.copy('test')
# print  pyperclip.paste()

###############################################

# import  re
# test='my number 1112-6610-9996'
#
# result = re.findall(r'\d{4}-\d{4}-\d{4}',test)
# print result
###############################################
# import shutil,os
# print os.getcwd()
# for i in  os.walk('D:\python\python2\Scripts\web\webtest'):
#     print i[0]
###############################################
# import zipfile
# test = zipfile.ZipFile('test.zip')
# test.namelist()
###############################################
def  test():
    com()
def  com():
    raise  Exception('test')
com()









