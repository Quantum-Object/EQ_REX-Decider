from REX import REX

def Equivalent_NFA_finder():
    rex1=REX(input("Regular Expression 1:").replace(" ", ""))
    N=rex1.to_NFA()
    print("Here is the Equivalent NFA :")
    N.show()
    
    