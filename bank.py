import os
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
adminPass = "Admin123"

cancel = False
accounts = []

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
    
clear()
while True:
    print("+ Welcome to pyBank! +\n\n[1] - Sign up\n[2] - Log In\n[3] - Admin Panel\n[0] - Quit")
    choice = input(">> ")

    if choice == '1':
        cancel = False
            
        #################################
        
        clear()
        while True:
            
            print("- Type 'CANCEL' anytime to leave! -\n")
            print("Insert the name of the account.")
            name = input(">> ")
            
            if name.lower() == 'cancel':
                clear()
                cancel = True
                break
            
            if not name:
                clear()
                print("- Insert a name! -\n")
                continue
            else:
                break
            
        if cancel:
            continue
        
        #################################
            
        clear()
        while True:
            print("- Type 'CANCEL' anytime to leave! -\n")
            print("Insert the email of the account.")
            email = input(">> ")
        
            if email.lower() == 'cancel':
                clear()
                cancel = True
                break
            
            if not email:
                clear()
                print("- Insert an email! -\n")
                continue
            
            if checkEmail(email) == True:
                break
            
        if cancel:
            continue
            
        #################################
            
        clear()
        while True:
            print("- Type 'CANCEL' anytime to leave! -\n")
            print("Insert the age of the account holder.")
            age_input = input(">> ").strip()
            
            if age_input.lower() == 'cancel':
                clear()
                cancel = True
                break

            try:
                age = int(age_input)
                if age < 18:
                    clear()
                    print("- Only people above the age of 18 can create an account. -\n")
                    continue
                else:
                    break
            except ValueError:
                clear()
                print("- Insert a number! -\n")
                continue
            
        if cancel:
            continue
            
        #################################
        
        clear()
        while True:
            print("- Type 'CANCEL' anytime to leave! -\n")
            print("Insert the password of the account.\n")
            print("+ REQUIREMENTS +\n- Minimum 6 characters\n- Maximum 16 characters\n- Must contain a number\n- Must contain an upper case letter\n- Must contain a special character among ('$','#','@','!','_','&')\n- Must not contain spaces\n")
            password = input(">> ")
            
            if password.lower() == 'cancel':
                clear()
                cancel = True
                break
            
            if not password:
                clear()
                print("- Insert a password! -\n")
                continue
            
            if checkPass(password) == True:
                break
            
        if cancel:
            continue
        
        #################################
        
        if not cancel:
            account = {
                "name": name,
                "email": email,
                "age": age,
                "password": password
            }
            clear()
            accounts.append(account)
            print("- Account created successfully! -\n")
        
    elif choice == '2':
        clear()
        print("wip")
    elif choice == '0':
        quit()
        break
    else:
        clear()
        print("- Insert an available option! -\n")