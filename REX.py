from NFA import NFA

#stirng 
#function to check if a sting can be made by it.

class REX:
    def __init__(self, s):
        self.s = s
        
    def w_to_NFA(s ):
        # this should only deal with the following form 
        # {w| w is a binary string not containing {*,+}}
        w=s
        N=NFA(len(w)+1,{},[len(w)+1])
        for i in range(1,N.q):
            N.f[i]=[(w[i-1],i+1)]
        return N
        
    def to_NFA(self):
        #here we turn a full Rex to NFA
        #for (11)*0 first this is (s1)*s2
        pass
    
    # this adds necessary .<concat> operator
    def add_conc(w):
        # first turn every for 1111*00-> 111.1*.00
        # also
        # 11100 -> 11100
        out=[]
        for i in range(0,len(w)-1):
            if w[i+1]=='*' and  w[i]!=')':
                out.append('.')
                out.append(w[i])
            else:
                out.append(w[i])
            if (w[i]=='*' and w[i+1] not in['|',')','(','.','*']):
                out.append('.')
        out.append(w[len(w)-1])
        return out
            
    # this collect char that belongs to alphabet together     
    def collect_strings(w):
        l=[]
        i=0
        while (i<len(w)):
            s=""
            if w[i] in ['|',')','(','.','*']:
                l.append(w[i])
                i+=1
            else:
                s=""
                while(i<len(w) and w[i] not in ['|',')','(','.','*']):
                    s+=w[i]
                    i+=1
                l.append(s)
        return l
        
        
    def RPN(w):
        #here we turn a string into a list of string representing rex in Postfix notation
        # for 11|0 -> [11 , 0 , |] 
        # for s1*|s2 -> [s1,*,s2,|]
        # for (s1 | s2)* -> [s1 , s2 , | , *]
        # for (s1 | s2 | s3) -> [s1 , s2 , s3 , | , |]
        # operators {*,|,.}
        # ok the big problem comes when w is like 11*0 this 1 , 1 ,* , 0
        pn=[]
        st=[]
        w=(REX.add_conc(w))
        w=REX.collect_strings(w)
        print(w)
        