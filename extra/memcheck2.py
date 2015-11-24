#from stackoverflow http://stackoverflow.com/questions/466684/how-can-i-return-system-information-in-python
#find memory output in system

import sys
if sys.platform == 'win32':
  import win32_sysinfo as sysinfo
elif sys.platform == 'darwin':
  import mac_sysinfo as sysinfo
elif 'linux' in sys.platform:
  import linux_sysinfo as sysinfo
#etc

print 'Memory available:', sysinfo.memory_available()
