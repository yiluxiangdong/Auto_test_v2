@echo off
taskkill /f /im pythonw.exe
del D:\python\python2\Lib\site-packages\robotide\contrib\testrunner\testrunner.pyc
python  D:\python\python2\Scripts\ride.py
pause