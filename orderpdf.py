#!/usr/bin/python
__author__ = 'dariogaravini'

import os
import os.path
import shutil

docks = '/scripts/docks'
setramar = '/scripts/setramar'
lloyd = '/scripts/lloyd'
eurodocks = '/scripts/eurodocks'
ifa = '/scripts/ifa'
cereol = '/scripts/cereol'
venezia = '/scripts/venezia'

uffici = [ docks, setramar ]
for dir in uffici:
        for file in os.listdir( dir ):
                if file.endswith('.pdf'):
#                       print (file)
                        corto = file[0:8]
                        lungo = os.path.join(dir,file[0:8])
#                       os.rename(os.path.join(dir, file),os.path.join(dir,file[0:8]))
#                       print (lungo)
                        if os.path.exists(os.path.join(dir,corto)):
                                print 'esiste'
                                shutil.move(os.path.join(dir, file),os.path.join(lungo,file))
                        else:
                                print 'non esiste'
                                os.makedirs(os.path.join(dir,corto))
                                shutil.move(os.path.join(dir, file),os.path.join(lungo,file))
