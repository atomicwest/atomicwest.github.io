# create excel sheet when procedure is run
"""
install packages via pip on Windows if 'Fatal error in launcher' error:
> python -m pip install pyodbc
> python -m pip install pandas
> python -m pip install xlsxwriter

1. run procedure that transforms and exports (SSMS)
2. procedure runs a select statment on result set to be exported (SSMS)
3. pass result set to Excel sheet (SSMS - pyodbc)
4. format result set into excel sheet (pandas/numpy)
5. add extra tabs for specific result set content (pandas/numpy)
"""

#install pyodbc from script instead of terminal???

##import pip
##
##lib = "pyodbc"
##
##pip.main(['install',lib])


import pyodbc as p

driver = 'SQL Server'
server = 'localhost'
server2 = ''
db = 'trial'
uid = 'Me'
pwd = 'password'

dsn = 'test'

#specify ODBC driver and other details
cnxn = p.connect('DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' %(driver,server,db,uid,pwd))

#use data source name (DSN)
cnxn = p.connect('DSN=%s;PWD=%s' % (dsn,pwd))

#create a cursor from connection
cursor = cnxn.cursor()
