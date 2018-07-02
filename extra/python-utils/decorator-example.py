#from https://www.youtube.com/watch?v=MYAEv3JoenI
def check(fxn):
    def proxy(a,b):
        if b==0:
            print('Cannot divide by 0')
        else:
            return fxn(a,b)
        
    return proxy


##div = check(div) #this is the same as adding the @check above div definition

@check
def div(a,b):
    return a/b

print(div(10,0))
print(div(10,5))
