import datetime as dt
import random as rn
from randomsayings import RandSaying

#filename is a string with the file  extension included
#method is character, either 'r', 'w', 'a'
#content is a list of strings to be written

def fileHandler(filename, method, content=[]):
    with open(filename, method) as file:
        if method == 'r':
            for line in file:
                print(line)
        elif method=='a' or method=='w':
            if method=='a':
                timestamp = str(dt.datetime.now()).split('.')[0]
                file.write("%s updated on %s %s\n" % (5*'-', timestamp, 5*'-') )
            for c in content:
                file.write("%s\n" % c)
        else:
            print('Method needs to be (r)ead, (w)rite, or (a)ppend')


def saveMprimes(n):
    out = []
    for j in range(n):
        out.append('The %i-th Mersenne prime is %i\n' % (j, 2**j - 1))
    return out



fname = 'info.txt'
phraseGenerator = RandSaying()
phraseGenerator.genSentences(10,'s')
fileHandler(fname, 'w', saveMprimes(20))
fileHandler(fname, 'r')
fileHandler(fname, 'a', phraseGenerator.sayings)
fileHandler(fname, 'r')
fileHandler(fname, 'w')
fileHandler(fname, 'r')
phraseGenerator.genSentences(12,'m')
fileHandler(fname, 'a', phraseGenerator.sayings)
fileHandler(fname, 'a', saveMprimes(20))
phraseGenerator.genSentences(12,'m')
fileHandler(fname, 'a', phraseGenerator.sayings)
fileHandler(fname, 'r')
