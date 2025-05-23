import os
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def clear():
    os.system("cls")

def quit():
    clear()
    print("- Goodbye! -\n")
    
def checkEmail(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        clear()
        print("- This email is not valid! -\n")
        
def checkPass(password):
    
    if (len(password) < 6 or len(password) > 12):
        clear()
        print("- This password is not valid! -\n")
        
    elif not re.search("[a-z]", password):
        clear()
        print("- This password is not valid! -\n")

    elif not re.search("[0-9]", password):
        clear()
        print("- This password is not valid! -\n")

    elif not re.search("[A-Z]", password):
        clear()
        print("- This password is not valid! -\n")

    elif not re.search("[$#@!_&]", password):
        clear()
        print("- This password is not valid! -\n")

    elif re.search("\s", password):
        clear()
        print("- This password is not valid! -\n")
        
    else:
        return True