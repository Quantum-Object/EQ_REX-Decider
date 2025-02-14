import networkx as nx
import matplotlib.pyplot as plt
import copy
from collections import deque
class NFA:
    def __init__(self, states, tran_func, accepted):
        self.q= states #: int (number of states)
        self.f = tran_func #: dict[int, list[tuple[str, int]]]  {1: ('a',2)) :: on recieving 'a' at state 1 go state 2}
        self.A = set(accepted) #: set<int> 
    # printing 
    def show(self):
        print("Q={", end="")
        for i in range(1, self.q + 1):
            print(f" {i}", end="")
        print(" }")
        print("Acc={", end="")
        for i in self.A:
            print(f" {i}", end="")
        print(" }")
        print("δ={")
        for i in self.f:
            for (a, b) in self.f[i]:
                print(f"  δ({i}, '{a}') -> {b}")
        print("}")
    

    #Union 
    def U(N1,N2):
        Un=NFA(N1.q+N2.q+1,{},set())
        l=N1.q+1
        Un.f[1]=[('ε',2),('ε',1+l)]
        for i in N1.f:
            Un.f[i+1]=[]
            for (a,b) in N1.f[i]:
                Un.f[i+1].append((a,b+1))
        for i in N2.f:
            Un.f[i+l]=[]
            for (a,b) in N2.f[i]:
                Un.f[i+l].append((a,b+l))
        for i in N1.A:
            Un.A.add(i+1)
        for i in N2.A:
            Un.A.add(i+l)
        return Un
    
    
    #kleene Star
    def S(self):
        sN= NFA(self.q+1,{},copy.deepcopy(self.A))
        #change no of states +1:
        sN.A = {state + 1 for state in sN.A}
        # change no of all nodes in tr_function
        sN.f[1]=[('ε',2)]
        for i in self.f:
             sN.f[i+1]=[]
             for (a,b) in self.f[i]:
                 sN.f[i+1].append((a,b+1))
        # from accepted to new start
        for  i in sN.A:
            if i in sN.f:
                sN.f[i].append(('ε',1))
            else:
                sN.f[i]=[]
                sN.f[i].append(('ε',1))
        # new state accepted to cover 'ε'
        sN.A.add(1)
        return sN        
    
    
    #concatination
    def Conc(N1,N2):
        N=NFA(N1.q+N2.q,copy.deepcopy(N1.f),copy.deepcopy(N2.A))
        N.A = {state + N1.q for state in N.A}
        for i in N1.A:
            if i not in N.f:
                N.f[i]=[]
            N.f[i].append(('ε',1+N1.q))
        for i in N2.f:
            N.f[i+N1.q]=[]
            for (a,b) in N2.f[i]:
                N.f[i+N1.q].append((a,b+N1.q))
        
        return N
                     
    #E_NFA Decider <decides if NFA has L=ϕ>
    def E_NFA(self):
        #the following code used DSU,DFS treating an NFA as a Graph
        #we are checking that (for all i in A -> i is not is DSU(1) )
        dsu=set()
        qu = deque()
        qu.append(1)
        while qu:
            state=qu.pop()
            dsu.add(state)
            for _, i in self.f.get(state, []):  
                if i not in dsu:
                    qu.append(i)
        has_A = any(i in dsu for i in self.A)
        return not has_A
    
    
    # this function is to find εpsilon_coluser of a state 
    def εpsilon_closure(self,state):
        closure={state}
        l=0
        while len(closure)!=l:
            l=len(closure)
            for a, s in self.f.get(state, []):
                if a == 'ε':
                    closure.add(s)
        return closure
            
        
    #function for following transitions and check if path valid
    def check_branch(self,state,i,w):
        if i==len(w):
            return any(state in self.A for state in self.εpsilon_closure(state))
        acc=False
        if state in self.f:
            for a,b in self.f[state]:
                if (a=='ε'):
                    acc= acc or self.check_branch(b,i,w)
                elif a==w[i]:
                    acc= acc or self.check_branch(b,i+1,w)
        return acc
        
      
    # A_NFA Decider <decides if NFA has accepts sting w>
    def A_NFA(self,w):
        # we gonna treat NFA as a graph and basically follow the transitions
        return self.check_branch(1,0,w)
             
             
    
# Visualization method
    def visualize(self):
        G = nx.DiGraph()

        # Add states (nodes)
        for state in range(1, self.q + 1):
            G.add_node(state, color='lightblue' if state not in self.A else 'lightgreen')

        # Add transitions (edges)
        for state in self.f:
            for (symbol, next_state) in self.f[state]:
                G.add_edge(state, next_state, label=symbol)

        # Draw the graph
        pos = nx.circular_layout(G)
        node_colors = [G.nodes[node]['color'] for node in G.nodes]
        edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}

        nx.draw(G, pos, with_labels=True, node_size=2000, node_color=node_colors, font_size=15, arrows=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        

        plt.title("NFA Visualization")
        plt.show()



