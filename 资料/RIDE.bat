@echo off 
@echo �ر�pythonw����
tasklist | find /i "pythonw.exe"&&taskkill /f /im pythonw.exe
@echo ɾ��testrunner.pyc�ļ�
if exist "D:\python\python2\Lib\site-packages\robotide\contrib\testrunner\testrunner.pyc" (del D:\python\python2\Lib\site-packages\robotide\contrib\testrunner\testrunner.pyc ) else (echo err)
@echo ����RIDE����
python  D:\python\python2\Scripts\ride.py
pause