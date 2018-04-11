import random as rn

articleSingle = [
            'The'
            ,'A'
            ]

articlePlural = [
            'Some'
            ,'Two'
            ,'Three'
            ,'Four'
            ,'Five'
            ,'Six'
            ,'Seven'
            ,'Eight'
            ,'Nine'
            ]

subject = [
            'donut'
            ,'tofu cube'
            ,'apple'
            ,'orange'
            ,'chicken'
            ,'plate'
            ,'pear'
            ,'jet'
            ,'can'
            ]

verb = [
        'sat'
        ,'ran'
        ,'jumped'
        ,'sang'
        ,'hopped'
        ,'read'
        ,'fell'
        ,'walked'
        ,'looked'
        ]
        
prep = [
        'on'
        ,'at'
        ,'in'
        ,'outside of'
        ,'inside of'
        ,'over'
        ,'under'
        ]
        
objects = [
        'counter'
        ,'sink'
        ,'stove'
        ,'refrigerator'
        ,'oven'
        ,'bowl'
        ,'cupboard'
        ]        

def rIdx(arr):
    return rn.randint(0,len(arr)-1)

def makeSentence(arts, artp, s,v, p, o, isPlural=False,):
    sentence = []
    
    if isPlural:
        sentence.append(artp[rIdx(artp)])
        sentence.append(s[rIdx(s)]+'s')
    else:
        prepos = arts[rIdx(arts)]
        subject = s[rIdx(s)]
        if prepos == 'A' and subject[0].lower() in 'aeiou':
            prepos = prepos+'n'
            
        sentence.append(prepos)
        sentence.append(subject)
        
    sentence.append(v[rIdx(v)])
    sentence.append(p[rIdx(p)])
    sentence.append('the')
    sentence.append(o[rIdx(o)])

    return ' '.join(sentence)
    

m1 = makeSentence(articleSingle, articlePlural, subject, verb, prep, objects)
m2 = makeSentence(articleSingle, articlePlural, subject, verb, prep, objects, True)
print(m1)
print(m2)


