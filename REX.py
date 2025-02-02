import NFA


#stirng 
#function to check if a sting can be made by it.

class REX:
    def __init__(self, s):
        self.s = s
        
    def to_NFA(s ):
        # this should only deal with the following form 
        # {w| w is a binary string not containing {*,+}}
        w=s
        N=NFA(len(w)+1,{},[len(w)+1])
        for i in range(1,N.q):
            N.f[i]=[(w[i-1],i+1)]
        return N
        
        
