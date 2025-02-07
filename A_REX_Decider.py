from REX import REX

def A_REX_Decider():
    rex=REX(input("Regular Expression :").replace(" ", ""))
    w=input("string w to be checked :")
    
    N=rex.to_NFA()
    if (N.A_NFA(w)):
        print(f"{w} ∈ L({rex.s}) ✅")
    else :
        print(f"{w} ∉ L({rex.s}) ❌")
    
    