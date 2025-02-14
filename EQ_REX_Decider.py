from REX import REX
import itertools
import time

def EQ_REX_Decider():
    start_time = time.perf_counter()
    rex1=REX(input("Regular Expression 1:").replace(" ", ""))
    rex2=REX(input("Regular Expression 2:").replace(" ", ""))
    alphabet=set()
    N1=rex1.to_NFA()
    N2=rex2.to_NFA()
    for c in rex1.s:
        if c not in {'|','*','(',')','.'}:
            alphabet.add(c)
    f=True   
    for i in range(1000):
        if int(time.perf_counter()-start_time)%7==0:
            print("Deciding ....")
        if (time.perf_counter()-start_time>10):
            print("most probably Equivalent")
            break
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
        print(f"L({rex1.s})= L({rex2.s}) ✅")
        

