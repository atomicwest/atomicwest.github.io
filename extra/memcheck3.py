#Devops| Ex2.py
#Jesson Go

#this code assumes a python interpreter is available on the system
#find and output 

import os
import platform
import sys

#import psutil

#return namedtuple of memory in bytes
#mem = psutil.virtual_memory()

#1. Total system memory 

#output variable
#tsm = mem.total
#tsm = "400"
#2. Total system memory in use

#output variable
#tsmIU = mem.used
#tsmIU = "500"
#3. Total system memory available

#for windows, available and free are the same parameter

#output variable
#tsmAV = mem.available
#tsmAV = 800

#------------------------------------------------------------------

#if windows is the detected operating system
#def memCheck():
if platform.system() == 'Windows' :
    #run the win32 library
    tsm = "output from the Windows commands"
    tsmIU = "output from the Windows commands"
    tsmAV = "output from the Windows commands"
elif platform.system()=='linux' or platform.system()=='linux2':
    #run the Linux commands
    linhand = open("/proc/meminfo", "r")
    tsm = linhand["MemTotal"]
    tsmAV = linhand["MemFree"]
    tsmIU = tsm - tsmAV
else:
    print("nothing")
    
#------------------------------------------------------------------

#in Linux, read from /proc/meminfo

#------------------------------------------------------------------

#output 1-3 in .txt file
outhand = open("Memout.txt", "w")
#outhand.write("Total System Memory: %s \nTotal System Memory in Use: %s \nTotal System Memory Available: %s" % (tsm, tsmIU, tsmAV))
outhand.write("Total System Memory: %s bytes \n" % tsm)
outhand.write("Total System Memory in use: %s bytes \n" % tsmIU)
outhand.write("Total System Memory available: %s bytes \n" % tsmAV)
outhand.close()
