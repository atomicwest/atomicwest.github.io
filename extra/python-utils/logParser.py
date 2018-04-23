'''
J. Go
Log parser, assumes logs are in the  following format:
YYYY-MM-DD HH:MM:SS.Msec | STATUS | notes with any chars #$%^
'''

import re

class logParser():
    def __init__(self, fname):
        self.targetFile = fname
        self.logs = []
        self.logLevelLogs = {}

    def parseLogs(self):
        fullString = ''
        with open(self.targetFile, 'r') as file:
            for line in file:
                fullString+=line
        pattern = r'\d{4}[-]\d{2}[-]\d{2}\ \d{2}[:]\d{2}[:]\d{2}.*'
        self.logs = re.findall(pattern,fullString)
        
        #hard-coded method for parsing logs by log level
        for log in self.logs:
            datePattern = r'\d{4}[-]\d{2}[-]\d{2}\ \d{2}[:]\d{2}[:]\d{2}'
            date = re.findall(datePattern,log)
            
            status = re.findall(r'[|][A-Z].*[|]', log)[0]
            status = re.findall(r'[A-Z]{1,10}', status)[0]
            
            details = re.findall(r'[|].*', log)[0]
            details = details.split('|')[-1]
            
            entry = 'Date: %s | Details: %s' % (date[0],details)
            
            if status in self.logLevelLogs.keys():
                self.logLevelLogs[status].append(entry)
            else:
                self.logLevelLogs[status] = [entry]
        
    def printLogs(self, logtype = 'n'):
        if logtype == 'n':
            for log in self.logs:
                print(log)
        elif logtype == 'l':
            for k in self.logLevelLogs.keys():
                print('-----%s-----' % k)
                for entry in self.logLevelLogs[k]:
                    print(entry)

l = logParser('GenLogs.txt')
l.parseLogs()
# l.printLogs()
l.printLogs('l')
# print(l.logLevelLogs['INFO'])
# print(l.logLevelLogs.keys())