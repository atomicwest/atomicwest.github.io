#Devops| Ex2.py

#this code assumes a python interpreter is available on the system
#find and output 

import os
from psutil import virtual_memory

#1. Total system memory 
mem = virtual_memory()
print(mem.total)
#memInBytes = os.sysconf('SC_PAGE_SIZE')*os.sysconf('SC_PHYS_PAGES')
#memInGB = memInBytes/(1024.**3)

#print(memInBtyes)
#print(memInGB)

#output variable
tsm = "200"

#2. Total system memory in use

#output variable
tsmIU = "300"

#3. Total system memory available

#output variable
tsmAV = "400"

#output 1-3 in .txt file
outhand = open("Memout.txt", "w")
outhand.write("Total System Memory: %s \n Total System Memory in Use: %s \n Total System Memory Available: %s" % (tsm, tsmIU, tsmAV))
outhand.close()
