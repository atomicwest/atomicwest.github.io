'''
J. Go
creates logs in the  following format:
YYYY-MM-DD HH:MM:SS.Msec | STATUS | notes with any chars #$%^$
'''

#import random sentence generator objects
from randomSayingClass import RandSaying

import re
import datetime as dt
import random as rn


class logGenerator():
    def __init__(self, logFname, randomWords=[''], pattern=''):
        self.logs = []
        self.logFile = logFname
        self.randomWords = randomWords
        self.pattern = pattern
        self.statuses = [
                        'INFO',
                        'TRACE',
                        'DEBUG',
                        'WARN',
                        'ERROR',
                        'FATAL'
                        ]
                        
    def createLogs(self,numLogs):
        for _ in range(numLogs):
            log = ''
            log+=str(dt.datetime.now())
            log+='|'
            log+=self.statuses[rn.randint(0,len(self.statuses)-1)]
            log+='|'
            nWords = len(self.randomWords)
            for _ in range(numLogs):
                log+= ' %s ' % self.randomWords[rn.randint(0,nWords-1)]
            self.logs.append(log)
    
    def saveLogsToFile(self, fname=''):
        if fname:
            filename = fname
        else:
            filename = self.logFile
        
        with open(filename, 'w') as file:
            for log in self.logs:
                file.write(log+'\n')
        
    def printLogs(self):
        for l in self.logs:
            print(l)


#---------------run test cases in console----------------------
n1 = RandSaying()
n1.genSentences(23, 'm')
notes = n1.sayings
print(notes)

g = logGenerator('GeneratedLogs.txt',notes)
g.createLogs(14)
g.printLogs()
g.saveLogsToFile()

