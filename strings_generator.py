from REX import REX
import itertools

def string_generator():
    rex=REX(input("Regular Expression :").replace(" ", ""))
    N=rex.to_NFA()
    t=int(input("generate strings of to length :"))
    count=0
    alphabet=set()
    for c in rex.s:
        if c not in {'|','*','(',')','.'}:
            alphabet.add(c)
    print(f'L{t} = {{')  
    for s in itertools.product(alphabet, repeat=t):
            w=(''.join(s) )
            if N.A_NFA(w):
                count+=1
                print(f"{w} ∈ L({rex.s}) ✅")
    print('}')
    print(f'L{t} is of size={count}')
    

    