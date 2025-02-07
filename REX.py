from NFA import NFA

#string 
#function to check if a sting can be made by it.

class REX:
    def __init__(self, s):
        self.s = s
        
    def w_to_NFA(s ): # O(n)
        # this should only deal with the following form 
        # {w| w is a binary string not containing {*,+}}
        w=s
        N=NFA(len(w)+1,{},[len(w)+1])
        for i in range(1,N.q):
            N.f[i]=[(w[i-1],i+1)]
        return N

    
    # this adds necessary .<concat> operator
    def add_conc(w): # O(n)
        n=len(w)
        # FINAAL time 
        # : loop1: when * is found a . is added after it only when the following char is in {'(','Σ'}
        out1=[]
        opt={')','|','.','*'}
        for i in range(n):
            out1.append(w[i])
            if w[i] == '*' and i + 1 < n and w[i + 1] not in opt:
                 out1.append('.')
        # loop2:when to add a . before *:
        w=out1
        out2=[]
        
        i=len(w)-1
        while(i>=0):
            out2.append(w[i])
            if w[i]=='*':
                if i-1>=0 and w[i-1]==')':
                    i-=1
                    while i>=0 and w[i]!='(':
                        out2.append(w[i])
                        i-=1
                    if (i>=0):
                        out2.append(w[i])
                    if i-1>=0 and  w[i-1] not in {'(','|','.','*'}:
                        out2.append('.')
                elif i-1>=0 and  w[i-1] not in {')','(','|','.','*'}:
                    out2.append(w[i-1])
                    i-=1
                    if i-1>=0 and  w[i-1] not in {')','(','|','.','*'}:
                        out2.append('.')
            i-=1
        out2.reverse()
        w=out2
        out = [w[0]]  # Start with the first character
        for i in range(1, len(w)):
            if (w[i-1] == ')' and w[i] == '(') or (w[i-1] not in opt and w[i] == '(') or (w[i-1] == ')' and w[i] not in opt ):
                out.append('.')
            out.append(w[i])
        return out
            
    # this collect char that belongs to alphabet together     
    def collect_strings(w):  #O(n)
        l=[]
        i=0
        while (i<len(w)):
            s=""
            if w[i] in {'|', ')', '(', '.', '*'}:
                l.append(w[i])
                i+=1
            else:
                s=[]
                while(i<len(w) and w[i] not in {'|', ')', '(', '.', '*'}):
                    s.append(w[i])
                    i+=1
                l.append("".join(s))
        return l
        
        
    def RPN(self):
        w=self.s
        #here we turn a string into a list of string representing rex in Postfix notation
        # for 11|0 -> [11 , 0 , |] 
        # for s1*|s2 -> [s1,*,s2,|]
        # for (s1 | s2)* -> [s1 , s2 , | , *]
        # for (s1 | s2 | s3) -> [s1 , s2 , s3 , | , |]
        # operators {*,|,.}
        # ok the big problem comes when w is like 11*0 this 1 , 1 ,* , 0
        
        w=(REX.add_conc(w)) #O(n)
        w=REX.collect_strings(w) #O(n)
        
        prn=[] #list to store postfix Expr.
        st=[] # stack
        
        #['(', 'aa', '|', 'b', ')', '*', '.', 'bbb']->[]
        
        #{*,.,|} proirty 
        opt={'*','.','|'}
        for c in w:
            if  c=='(':
                st.append(c)
            elif c in opt:
                while len(st)>0 and st[-1] in opt and  st[-1]<c:
                    prn.append(st.pop())
                st.append(c)
            elif c==')':
                while len(st)>0 and st[-1]!='(':
                    prn.append(st.pop())
                st.pop()
            else:
                prn.append(c)
        while (len(st)!=0):
            prn.append(st.pop())
        
        return prn
    
    def to_NFA(self):
        prn=self.RPN()
        st=[]
        opt={'*','.','|'}
        for i in prn:
            if i not in opt:
                st.append(REX.w_to_NFA(i))
            else:
                N1=st.pop()
                if i=='*':
                    st.append(N1.S())
                elif i=='.':
                    N2=st.pop()
                    st.append(NFA.Conc(N2,N1))
                else:
                    N2=st.pop()
                    st.append(NFA.U(N2,N1))
        return st[-1]
