#generate a test directory with subdirectories and files

import os
import random 

root = "rootdir"

def gennums(n):
    out = []
    upperend = n*100
    padding = len(str(upperend))
    
    for i in range(n):
        nextnum = random.randint(n, n*100)
        numstring = str(nextnum).zfill(padding) 
        out.append(numstring)
        
    return out

def touch(dir):
    name = str(random.randint(10,1000)).zfill(4)
    with open(dir+"/"+name, 'a'):
        os.utime(dir+"/"+name, None)
    
def makedir():
    n = 10
    os.makedirs(root)
    nums = gennums(n)
    
    for i in range(n):
        nextdir = nums.pop()
        nextfolder = root + "/" + nextdir
        os.makedirs(nextfolder)
        touch(nextfolder)
    
if __name__=="__main__":
    makedir()
