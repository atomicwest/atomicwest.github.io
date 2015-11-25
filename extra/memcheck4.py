#Devops| Ex2.py
#Jesson Go

#this code assumes a python interpreter is available on the system
#find system memory and output to text file
#figure out how much memory is being "wasted"

#+ should find the total memory
#- find the in use memory
#- free -m "free" is the free of interest and should be the difference
#of in use

import os
import platform
import sys
import ctypes

#------------------------------------------------------------------
#use conditionals to check OS
#if windows is the detected operating system
#def memCheck():
if 'Windows' in platform.system():
    #run the win32 library
    #in use memory = total - available?
    class MEMORYSTAT(ctypes.Structure):
        #generate list of 2 tuples with field names and long type
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
            super(MEMORYSTAT, self).__init__()

    stat = MEMORYSTAT()
    #call GlobalMemoryStatusEx from Windows to store memory info
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))

    #access system stats from the stored list data
    tsm = stat.ullTotalPhys / 1024
    tsmAV = stat.ullAvailPhys / 1024
    #tsmIUA = tsm - tsmAV
    #memory load is a percentage
    tsmMemLo = stat.dwMemoryLoad
    tsmIU = tsmMemLo * tsm / 100
    print(tsmMemLo)

#if Linux is detected
elif 'Linux' in platform.system():
    #read out of /proc/meminfo
    meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
    #total system memory
    tsm = meminfo['MemTotal']
    
    tsmFr = int(meminfo['MemFree'])
    tsmCa = int(meminfo['Cached'])
    tsmBu = int(meminfo['Buffers'])
    
    #total memory in use, accounting for Cache and Buffers
    #MemTotal + Buffers + Cached - (MemFree + Cached) = Actual Used
    #MemTotal + Buffers + - MemFree = Actual Used
    tsmIU = int(tsm) + tsmBu + - tsmFr

    #total available memory, Memfree is the actual available minus cached
    #actual available = meminfo['MemFree'] + meminfo['Cached']
    tsmAV = tsmFr + tsmCa
    
else:
    print("Unrecognized OS")
    
#test by printing variables to the console
print("Total system memory: %d kB" % tsm)
print("Total available system memory: %d kB" % tsmAV)
print("Total system memory in use: %d kB" % tsmIU)
#print("Total system memory in use (original Calc): %d kB" % tsmIUA)

#------------------------------------------------------------------

#output 1-3 in .txt file
outhand = open("Memout.txt", "w")
#outhand.write("Total System Memory: %s \nTotal System Memory in Use: %s \nTotal System Memory Available: %s" % (tsm, tsmIU, tsmAV))
outhand.write("Total System Memory: %s bytes \n" % tsm)
outhand.write("Total System Memory in use: %s bytes \n" % tsmIU)
outhand.write("Total System Memory available: %s bytes \n" % tsmAV)
outhand.close()
