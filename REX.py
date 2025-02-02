import NFA


#stirng 
#function to check if a sting can be made by it.

class REX:
    def __init__(self, s):
        self.s = s
        
    def to_NFA(self):
        # (*,+,|) and (0,1) or (a,b,c)
        # so now we should look for brackets and strat parsing them in some stack manner
        # for instance
        #1. break s into ()()()().... 
        #2. make NFA for each of these:
        #3. so now make subNFA OK
        # a string is 
        """ 
        (X)->X
        X+Y-> Conc(X,Y)
        ua*b-> Conc(u,conc(a.S(),b))
        X|Y-> union(X,Y)
        
        """
        
            
            

            
        
        
        
        # what can we have now with no brackets well:
        # like (1*0 or 1+1+0 clearly we have to take it in account 1111==1+1+1+1 
        #now priorty of operation as follows:
        # star,conc,union (*,+,|)
        # for r1*r2+r3|r4
        # this means we should do it recursively starting from | and then + then *