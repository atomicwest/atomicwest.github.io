'''
J. Go

csv filehandler 
assumes top row holds column headers

'''

import numpy as np
import matplotlib as mpl
import datetime as dt
import random as rd

def csvhandler(fname):
    #each row in textfile must have same number of values
    pass
    # np.loadtxt = 

'''    
expects a number from 0 to inf to be passed, will return
equivalent alphabetic letter sequence
n=0 returns 'A', n=26 returns 'AA'
only works up to 'ZZ'
'''
def excelCols(n):
    output = ''
    numLetters = int(n/26)+1
    # front = chr(numLetters+65)
    if n < 26:
        output+=chr(n + 65)
    else:
        firstletterNum = int(n/26)
        output+=chr(firstletterNum + 64)
        
        padding = n-(26*int(n/26))
        output+=chr(padding+65)
    return output
    
def genRandCSV(numCol, numRow, fname='test.csv'):
    # all columns are of the same length
    
    records = []
    for i in range(numCol):
        nowtime = dt.datetime.now()
        rnum = rd.randint(1,10)
        
        columnHeader = np.array(['Column %s' % excelCols(i)])
        
        if nowtime.microsecond%2 == 0:
            columnItems = np.linspace(rnum,rnum*10,numRow)
        else:
            columnItems = [i**2 for i in range(rnum, rnum+numRow)]
        columnItems = [str(ci) for ci in columnItems]
        # print(columnHeader)
        # print(columnItems)
        x = np.concatenate((columnHeader, columnItems), axis=0)
        records.append(x)
    
    with open(fname,'w') as file:
        np.savetxt(file, np.transpose(records), delimiter=',', fmt='%s')   # x,y,z equal sized 1D arrays
    
genRandCSV(30,50, 'randarr.csv')
# print(excelCols(0))
# print(excelCols(26))
# print(excelCols(56))
# print(excelCols(127))
