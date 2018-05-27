import random as rn
import datetime as dt

class sqlGen():
    def __init__(self):
        self.primewords = [
            'strawberry',
            'maple',
            'key lime',
            'dragonfruit',
            'cookies and cream',
            'matcha green tea',
            'tres leches',
            'horchata',
            'chocolate'
            ]
    
    def genScript(self, numrec, numcol, tblname, stamp, createInsert, fname="genGlazeRows.sql"):
        with open(fname, 'w') as file:
            file.write('--TransactSQL generated with Python on %s\n\n' % str(dt.datetime.now()))
            
            #set up columns  first
            schema = ['col' + chr(i) for i in range(65,65+numcol)]
            
            if createInsert:
                #generate create statement first
                #second, second to last, and last are varchar, else float
                file.write('CREATE TABLE %s (\n' % tblname)
                for i,s in enumerate(schema):
                    if i not in [1,len(schema)-2, len(schema)-1]:
                        file.write('\t%s FLOAT,\n' % s)
                    elif i != len(schema)-1:
                        file.write('\t%s VARCHAR(100),\n' % s)
                    else:
                        file.write('\t%s VARCHAR(100)\n' % s)
                file.write(')\n\n\n')
                
                #generate insert statement
                file.write('INSERT INTO %s ( \n' % tblname)
                for i,s in enumerate(schema):
                    if i < len(schema)-1:
                        file.write('\t%s,\n' % s)
                    else:
                        file.write('\t%s\n' % s)
                file.write(')\n\n')
            
            schema = str(schema)[1:-1]
            schema = schema.replace("'","")
            
            #create actual result set
            if not createInsert:
                file.write('SELECT * FROM ( \n')
            
            file.write('VALUES \n')
            
            
            for i in range(numrec):
               record = '('
               record += str(1000+i)+','
               record += "'" + self.primewords[rn.randint(0,len(self.primewords)-1)] + "'" + ','
               otherrecords = [str(rn.randint(1,100) + rn.random()) for _ in range(numcol-4)]
               otherrecords = str(otherrecords).replace("'","")[1:-1]
               record+=otherrecords
               record+= "," + "'" + str(dt.datetime.now()) + "'"
               record+= "," + "'" + stamp + "'"
               record += ')'
               if i != numrec-1:
                   record+=",\n"
               else:
                   record+="\n"
               file.write(record)
                
            if not createInsert:
                file.write(') AS %s\n' % tblname)
                file.write('(%s);' % schema)
            else:
                file.write(';\n')
        
        
s = sqlGen()
s.genScript(1000,11,'glazes2', 'Glaze2', True, "genGlazeCreateProc.sql")   #will create script for create/insert table
s.genScript(1000,11,'glazes2', 'Glaze2', False, "genGlazeValues.sql")       #only creates a select statement