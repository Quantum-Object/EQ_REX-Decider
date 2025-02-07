from A_REX_Decider import A_REX_Decider
from strings_generator import string_generator


def main():
    print("Hello!")
    print("for string generator press 1️⃣")
    print("for checking w ∈ L(rex) press 2️⃣")
    inp=input()
    if inp=='2':
        A_REX_Decider()
    elif inp=='1':
        string_generator()
    else:
        print("You entered a wrong input 😕")
    
        

main()