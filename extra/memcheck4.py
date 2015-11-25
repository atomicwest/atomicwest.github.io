#Devops| Ex2.py
#Jesson Go

#this code assumes a python interpreter is available on the system
#find and output 

import os
import platform
import sys

#for using MEMORYSTATUSEX
import ctypes

#------------------------------------------------------------------

#if windows is the detected operating system
#def memCheck():
if 'Windows' in platform.system():
    #run the win32 library
    #in use memory = total - available?
    class MEMORYSTATUSEX(ctypes.Structure):
        _fields_ = [
            ("dwLength", ctypes.c_ulong),
            ("dwMemoryLoad", ctypes.c_ulong),
            ("ullTotalPhys", ctypes.c_ulonglong),
            ("ullAvailPhys", ctypes.c_ulonglong),
            ("ullTotalPageFile", ctypes.c_ulonglong),
            ("ullAvailPageFile", ctypes.c_ulonglong),
            ("ullTotalVirtual", ctypes.c_ulonglong),
            ("ullAvailVirtual", ctypes.c_ulonglong),
            ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        def __init__(self):
            #initialize to size of MEMORYSTATUSEX
            self.dwLength = ctypes.sizeof(self)
            super(MEMORYSTATUSEX, self).__init__()

    stat = MEMORYSTATUSEX()
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))

    tsm = stat.ullTotalPhys / 1024
    tsmAV = stat.ullAvailPhys / 1024
    tsmIU = tsm - tsmAV
    
elif 'Linux' in platform.system():
    #read out of /proc/meminfo
    meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
    #total system memory
    tsm = meminfo['MemTotal']
    #total available memory, assuming MemFree also contains Cached and/or buffer
    tsmAV = meminfo['MemFree']
    #total memory in use, assuming that it is a simple difference
    #between total and available
    tsmIU = int(tsm) - tsmAV
else:
    print("Unrecognized OS")
    
#test by printing variables to the console
print("Total system memory: %d kB" % tsm)
print("Total available system memory: %d kB" % tsmAV)
print("Total system memory in use: %d kB" % tsmIU) 

#------------------------------------------------------------------

#output 1-3 in .txt file
outhand = open("Memout.txt", "w")
#outhand.write("Total System Memory: %s \nTotal System Memory in Use: %s \nTotal System Memory Available: %s" % (tsm, tsmIU, tsmAV))
outhand.write("Total System Memory: %s bytes \n" % tsm)
outhand.write("Total System Memory in use: %s bytes \n" % tsmIU)
outhand.write("Total System Memory available: %s bytes \n" % tsmAV)
outhand.close()
