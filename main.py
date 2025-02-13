from A_REX_Decider import A_REX_Decider
from strings_generator import string_generator
from EQ_REX_Decider import EQ_REX_Decider
from Equivalent_NFA_finder import Equivalent_NFA_finder
def main():
    print("Hello!")
    print("for string generator press 1️⃣")
    print("for checking w ∈ L(rex) press 2️⃣")
    print("for checking L(rex1) = L(rex2) press 3️⃣")
    print("for finding Equivalent NFA press 4️⃣")

    inp=input()
    if inp=='2':
        A_REX_Decider()
    elif inp=='1':
        string_generator()
    elif inp=='3':
        EQ_REX_Decider()
    elif inp=='4':
        Equivalent_NFA_finder()
    else:
        print("You entered a wrong input 😕")
    
        
main()