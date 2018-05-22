'''
J. Go
5/21/2018
creates sql script to be run in ssms
    script will create a table with random values
'''
import random as rn
import datetime as dt

class sqlGen():
    def __init__(self):
        self.primewords = [
            'strawberry',
            'maple',
            'original',
            'cookies and cream',
            'matcha green tea',
            'tres leches',
            'horchata',
            'chocolate'
            ]
    
    def genScript(self, numrec, numcol, tblname, fname="genRows.sql"):
        with open(fname, 'w') as file:
            file.write('--TransactSQL generated with Python\n')
            file.write('SELECT * FROM ( VALUES\n')
            for i in range(numrec):
               record = '('
               record += str(1000+i)+','
               record += "'" + self.primewords[rn.randint(0,len(self.primewords)-1)] + "'" + ','
               otherrecords = [str(rn.randint(1,100) + rn.random()) for _ in range(numcol-3)]
               otherrecords = str(otherrecords).replace("'","")[1:-1]
               record+=otherrecords
               record+= "," + "'" + str(dt.datetime.now()) + "'"
               record += ')'
               if i != numrec-1:
                   record+=",\n"
               else:
                   record+="\n"
               file.write(record)
                
            schema = ['col' + chr(i) for i in range(65,65+numcol)]
            schema = str(schema)[1:-1]
            schema = schema.replace("'","")
            file.write(') AS %s\n' % tblname)
            file.write('(%s);' % schema)
        
        
        
s = sqlGen()
s.genScript(10,7,'glazes')
        