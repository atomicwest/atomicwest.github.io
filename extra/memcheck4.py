#Devops| Ex2.py
#Jesson Go

#this code assumes a python interpreter is available on the system
#find and output 

import os
import platform
import sys

#regular expressions e.g. search
import re

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
if 'Windows' in platform.system() :
    #run the win32 library
    #in use memory = total - available?
    tsm = "output from the Windows commands"
    tsmIU = "output from the Windows commands"
    tsmAV = "output from the Windows commands"
    
elif 'Linux' in platform.system():
    #read out of /proc/meminfo
    meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
    #total system memory
    tsm = meminfo['MemTotal']
    #total available memory
    tsmAV = meminfo['MemFree']
    #total memory in use, assuming that it is a simple difference
    #between total and available
    tsmIU = int(tsm) - tsmAV
else:
    print("Unrecognized OS")
    
#------------------------------------------------------------------

#in Linux, read from /proc/meminfo

#------------------------------------------------------------------

#output 1-3 in .txt file
outhand = open("Memout.txt", "w")
outhand.write("Total System Memory: %s kB \n" % tsm)
outhand.write("Total System Memory in use: %s kB \n" % tsmIU)
outhand.write("Total System Memory available: %s kB \n" % tsmAV)
outhand.close()
