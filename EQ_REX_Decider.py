from REX import REX
import itertools

def EQ_REX_Decider():
    rex1=REX(input("Regular Expression 1:").replace(" ", ""))
    rex2=REX(input("Regular Expression 2:").replace(" ", ""))
    alphabet=set()
    N1=rex1.to_NFA()
    N2=rex2.to_NFA()
    for c in rex1.s:
        if c not in {'|','*','(',')','.'}:
            alphabet.add(c)
    f=True   
    print(alphabet)
    for i in range(300):
        for s in itertools.product(alphabet, repeat=i):
            w=(''.join(s) )
            acc1=N1.A_NFA(w) 
            acc2=N2.A_NFA(w) 
            if not(acc1==acc2) :
                print(f"L({rex1.s}) ≠ L({rex2.s}) ❌")
                print(f"first string different : {'ε (empty string)' if w=="" else w} is accepted only by {rex1.s if acc1 else rex2.s} ")
                f=False
            if not f : break
        if not f : break
    if (f):
        print(f"l({rex1.s})≠ L({rex2.s}) ✅")
        
