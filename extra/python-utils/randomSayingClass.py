import random as rn

class RandSaying():
    def __init__(self):
        self.sayings = []
        self.articleSingle = [
            'The'
            ,'A'
            ]
        self.articlePlural = [
            'Some'
            ,'Two'
            ,'Three'
            ,'Four'
            ,'Five'
            ,'Six'
            ,'Seven'
            ,'Eight'
            ,'Nine'
            ,'Many'
            ]
        
        self.subject = [
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

        self.verb = [
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
        
        self.prep = [
            'on'
            ,'at'
            ,'in'
            ,'outside of'
            ,'inside of'
            ,'over'
            ,'under'
            ]
        
        self.objects = [
            'counter'
            ,'sink'
            ,'stove'
            ,'refrigerator'
            ,'oven'
            ,'bowl'
            ,'cupboard'
            ]        

    
    def __str__(self):
        return """ 
        
        Instantiates a random sentence generator
        
        methods:
        .genSentences(n, t):
            n = number of sentences
            t = sentence types: 
                's' singular subject
                'p' plural subject
                'm' for mixed 
        .printSentences()
        """
    
    def genSentences(self, numSentences, sentType='m'):
        
        randSentences = []
        
        #-----------------------------------------------
        def makeSentence(isPlural=False):
            
            def rIdx(arr):
                return rn.randint(0,len(arr)-1)
    
            sentence = []
        
            if isPlural:
                sentence.append(self.articlePlural[rIdx(self.articlePlural)])
                sentence.append(self.subject[rIdx(self.subject)]+'s')
            else:
                prepos = self.articleSingle[rIdx(self.articleSingle)]
                subject = self.subject[rIdx(self.subject)]
                if prepos == 'A' and subject[0].lower() in 'aeiou':
                    prepos = prepos+'n'
                    
                sentence.append(prepos)
                sentence.append(subject)
                
            sentence.append(self.verb[rIdx(self.verb)])
            sentence.append(self.prep[rIdx(self.prep)])
            sentence.append('the')
            sentence.append(self.objects[rIdx(self.objects)])
        
            return ' '.join(sentence) + '.'
        #-----------------------------------------------
        
        for i in range(numSentences):
            if sentType=='m':
                flag = bool(rn.randint(0,1))
                
            elif sentType=='p':
                flag = True
            else:
                flag = False
                
            randSentences.append(makeSentence(flag))
            
        self.sayings = randSentences

    def printSentences(self):
        print(20*'-')
        for l in self.sayings:
            print(l)
        print(20*'-')

#---------run test cases in the console-------------------
# o1 = RandSaying()
# print(o1)
# o2 = RandSaying()
# o3 = RandSaying()

# o1.genSentences(25, 'm')
# o2.genSentences(1,'s')
# o3.genSentences(14,'p')

# o1.printSentences()
# o2.printSentences()
# o3.printSentences()

# o2.genSentences(12,'s')
# o2.printSentences()
