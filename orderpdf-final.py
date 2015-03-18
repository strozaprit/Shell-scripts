#!/usr/bin/python
__author__ = 'dariogaravini'

import os
import os.path
import shutil

docks = '/home/w1/scanner/archiviobolle/Docks'
setramar = '/home/w1/scanner/archiviobolle/Setramar'
lloyd = '/home/w1/scanner/archiviobolle/Lloyd'
eurodocks = '/home/w1/scanner/archiviobolle/Eurodocks'
ifa = '/home/w1/scanner/archiviobolle/Ifa'
cereol = '/home/w1/scanner/archiviobolle/Cereol'
ravenna = '/home/w1/scanner/archiviobolle/Ravenna'

uffici = [ docks, setramar, lloyd, eurodocks, ifa, cereol, ravenna ]
for dir in uffici:
        for file in os.listdir( dir ):
                if file.endswith('.pdf'):
#                       print (file)
                        corto = file[0:8]
                        lungo = os.path.join(dir,file[0:8])
#                       print (lungo)
                        if os.path.exists(os.path.join(dir,corto)):
#                                print 'esiste'
                                shutil.move(os.path.join(dir, file),os.path.join(lungo,file))
                        else:
#                                print 'non esiste'
                                os.makedirs(os.path.join(dir,corto))
                                os.chmod(os.path.join(dir,corto), 0777)
                                shutil.move(os.path.join(dir, file),os.path.join(lungo,file))
