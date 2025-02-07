from A_REX_Decider import A_REX_Decider
from strings_generator import string_generator


def main():
    print("Hello!")
    print("for string generator press 1")
    print("for checking w ∈ L(rex) press 2")
    inp=input()
    if inp=='1':
        A_REX_Decider()
    elif inp=='2':
        string_generator()
    else:
        print("You entered a wrong input 😕")
    
        

main()