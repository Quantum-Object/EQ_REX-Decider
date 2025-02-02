import REX
import copy
class NFA:
    def __init__(self,states,tran_func,accepted):
        self.q=states
        self.f=tran_func
        self.A=accepted
    
    # Complement
    def c(self):
        cNFA= NFA(self.q,copy.deepcopy(self.f),[])
        for i in range(1,self.q+1):
            if i not in self.A:
                cNFA.A.append(i)
        return cNFA

    #Union 
    def U(N1,N2):
        Un=NFA(N1.q+N2.q+1,{},[])
        l=N1.q+1
        Un.f[1]=[('ε',2),('ε',1+l)]
        for i in N1.f:
            Un.f[i+1]=[]
            for (a,b) in N1.f[i]:
                Un.f[i+1].append((a,b+1))
        for i in N2.f:
            Un.f[i+l]=[]
            for (a,b) in N1.f[i]:
                Un.f[i+l].append((a,b+l))
        for i in N1.A:
            Un.A.append(i+1)
        for i in N2.A:
            Un.A.append(i+l)
        return Un
    
    #Intersection 
    def I(N1,N2):
        return NFA.c(NFA.U(NFA.c(N1),NFA.c(N2)))
    
    #kleene Star
    def S(self):
        sN= NFA(self.q+1,{},copy.deepcopy(self.A))
        #change no of states +1:
        for i in range(len(self.A)):
             sN.A[i]+=1
        # change no of all nodes in tr_function
        for i in self.f:
             sN.f[i+1]=[]
             for (a,b) in self.f[i]:
                 sN.f[i+1].append((a,b+1))
        sN.f[1]=[('ε',2)]
        # from accepted to new start
        for  i in sN.A:
            if i in sN.f:
                sN.f[i].append(('ε',1))
            else:
                sN.f[i]=[]
                sN.f[i].append(('ε',1))
        # new state accepted to cover 'ε'
        sN.A=[1]+sN.A
        return sN        
    
    
    #concatination
    def Conc(N1,N2):
        N=NFA(N1.q+N2.q,copy.deepcopy(N1.f),copy.deepcopy(N2.A))
        for i in range(len(N2.A)):
            N.A[i]+=N1.q
        for i in N2.f:
            N.f[i+N1.q]=[]
            for (a,b) in N2.f[i]:
                N.f[i+N1.q].append((a,b+N1.q))
        for i in N2.A:
            if i not in N.f:
                N.f[i]=[]
            N.f[i].append(('ε',1+N1.q))
        return N
            
               
        
             
             
    
        
n=NFA(2,{1:[('a',2)]},[2])


N=NFA.Conc(n,n)
print(N.q,N.A,N.f)

    
        
        
        

        
        
        