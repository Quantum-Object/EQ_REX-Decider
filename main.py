from REX import REX
from NFA import NFA



def main():
    rex=REX(input("Regular Expression :").replace(" ", ""))
    
    N=rex.to_NFA()
    print("Equavilant NFA :")
    N.show()
    for i in range(100):
        w= bin(i)[2:]
        s1=w.replace('1', 'a').replace('0', 'b')
        s2=w.replace('0', 'a').replace('1', 'b')
        t=N.A_NFA(s1)
        t2=N.A_NFA(s2)
        if t:
            print(f"{s1} ∈ L({rex.s}) ✅")
        if t2:
            print(f"{s2} ∈ L({rex.s}) ✅")
        

#(a|b*)(a|b)
main()