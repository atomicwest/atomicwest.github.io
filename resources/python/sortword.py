'''
word sorter

'''

import random as r

def sortWord(word):
    newWord = []
    w = [l for l in word]
    banList = [" ", ","]
    while len(w) > 0:
        j = r.randint(0,len(w)-1)
        if w[j] not in banList:
            newWord.append(w[j])
        w.remove(w[j])
    return combineStringList(newWord)

def combineStringList(sl):
    out = ""
    for l in sl:
        out+=l
    return out


test = "jesson go"
print(sortWord(test))
