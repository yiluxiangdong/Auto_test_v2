#!usr/bin/env python
#-*- coding:utf-8 _*-
import os,sys,time

def createLib():
    if len(sys.argv)==1:
        Libname = raw_input('>>>>Enter a custom package name:')
    else:
        Libname = sys.argv[1]

    if Libname.strip()!='':
        Libname = Libname.capitalize()
        Libpath = 'D:\python\python2\Lib\site-packages\{}'.format(Libname)
        if os.path.exists(Libpath):
            print 'Custom packages already exist'
        else:
            os.mkdir(Libpath)
            print 'Custom package does not exist, recreate the package {}'.format(Libname)
        with open(r'{}\_init_.py'.format(Libpath), 'wb') as fn:
            fn.write('#!usr/bin/env python\n#-*- coding:utf-8 _*- \n\nfrom {} import {}\n__verison__ = "0.1.1"\n\nclass {}({}):\n\tROBOT_LIBRARY_SCOPE = "GLOBAL"'.format(Libname,Libname,Libname,Libname))
        with open(r'{}\{}.py'.format(Libpath, Libname), 'wb') as fn:
            fn.write("#!usr/bin/env python\n#-*- coding:utf-8 _*-\n\nimport *\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nclass {}:\n\tdef __init__(self):\n\t\tpass\n\n\tdef __del__(self):\n\t\tpass\n\nif __name__ == '__main__':\n\t{}={}()".format(Libname,Libname.lower(),Libname))
        print 'createLib success {}'.format(Libname)
		 
    else:
        print 'Input unlawful'


if __name__ == '__main__':
    createLib()


