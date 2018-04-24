'''
J.Go
Parse sample apache logs in the following format:

###.###.###.### - - [DD/Mon/YYYY:HH:MM:SS -Msec] "HTTPMETHOD /url/for/something HTTP/1.1" HTTPSTATUSCODE ####
OR 
web.domain - - [DD/Mon/YYYY:HH:MM:SS -Msec] "HTTPMETHOD /url/for/something HTTP/1.1" HTTPSTATUSCODE ####
'''

import re

def apacheParser(fname, save=False,savename='apachelogs.csv'):
    fullstring = ''
    with open(fname, 'r') as file:
        for line in file:
            fullstring+=line
    
    csvLines = ['IP/Domain,DateStamp,Message,HTTPStatus\n']
    
    logs = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*|[A-Za-z0-9]*\.[A-Za-z0-9]*\.\w{2,4}.*', fullstring)
    for l in logs:
        line = ''
        # print(l)
        ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[A-Za-z0-9]*\.[A-Za-z0-9]*\.[a-z]{2,4}',l)[0]
        datestamp = re.findall('\[.*\](?!".*")',l)[0]
        if len(datestamp) > 30:
            datestamp = datestamp[0:28]
        message = re.findall('\".*\"',l)[0]
        HTTPcode = re.findall('\" \d{3}', l)[0].split()[-1]
        line = ('%s,%s,%s,%s\n' % (ip,datestamp,message,HTTPcode))
        csvLines.append(line)
        # print(ip)
        # print(datestamp)
        # print(message)
        # print(HTTPcode)
        
    if save:
        with open(savename, 'w') as file:
            for line in csvLines:
                file.write(line)
                
filename = "apacheTestLog.txt" 
apacheParser(filename, True)