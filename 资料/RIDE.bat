@echo off 
@echo 关闭pythonw进程
tasklist | find /i "pythonw.exe"&&taskkill /f /im pythonw.exe
@echo 删除testrunner.pyc文件
if exist "D:\python\python2\Lib\site-packages\robotide\contrib\testrunner\testrunner.pyc" (del D:\python\python2\Lib\site-packages\robotide\contrib\testrunner\testrunner.pyc ) else (echo err)
@echo 启动RIDE工具
python  D:\python\python2\Scripts\ride.py
pause