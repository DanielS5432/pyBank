from func import *

import json
import os
import bcrypt

file_path = "db/accounts.json"

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        json.dump([], f)

with open(file_path, "r") as f:
    try:
        accounts = json.load(f)
    except json.JSONDecodeError:
        accounts = []

adminPass = "Admin123"
cancel = False
    
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
                elif age > 100:
                    clear()
                    print("- Too old! -\n")
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
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            
            account = {
                "name": name,
                "email": email,
                "age": age,
                "password": hashed_password,
                "money": 0
            }
            clear()
            accounts.append(account)

            with open(file_path, "w") as f:
                json.dump(accounts, f, indent=4)

            print("- Account created successfully! -\n")
        
    elif choice == '2':
        clear()
        print("wip")
    elif choice == '3':
        cancel = False
            
        #################################
        
        clear()
        while True:
            print("- Type 'CANCEL' anytime to leave! -\n")
            print("Insert the admin password.")
            admin_inp = input(">> ")

            if admin_inp.lower() == 'cancel':
                clear()
                cancel = True
                break

            if not admin_inp:
                clear()
                print("- Insert a password! -\n")
                continue

            if admin_inp == adminPass:
                clear()
                while True:
                    print("+ Admin Panel +\n\n[1] - Accounts List\n[2] - Remove Account\n[3] - Manage Money\n[0] - Quit")
                    admchoice = input(">> ")

                    if admchoice == '1':
                        cancel = False
                        clear()
                        
                        if not accounts:
                            print("- There are no accounts yet! -\n")
                            cancel = True
                            
                        if cancel == True:
                            continue
                        
                        i = 1
                        for account in accounts:
                            print(f"- Account Number {i}-\n\n+ Name - {account['name']}\n+ Email - {account['email']}\n+ Age - {account['age']}\n+ Money - {account['money']}\n")
                            i += 1
                        input("- Insert anything to leave. -\n>> ")
                        clear()
                        
                    elif admchoice == '2':
                        cancel = False
                        clear()
                        
                        if not accounts:
                            print("- There are no accounts yet! -\n")
                            cancel = True
                            
                        if cancel == True:
                            continue
                        
                        while True:
                            print("- Type 'CANCEL' anytime to leave! -\n")
                            print("Insert the number of the account you want to remove.")
                            removeid_inp = input(">> ")
                            
                            if removeid_inp.lower() == 'cancel':
                                clear()
                                cancel = True
                                break
                            
                            try:
                                removeid = int(removeid_inp)
                                if removeid < 1 or removeid > len(accounts):
                                    clear()
                                    print("- This account number does not exist! -\n")
                                    continue
                                clear()
                                accounts.pop(removeid - 1)
                                print(f"- Account with the number {removeid} removed! -\n")
                                break
                            except ValueError:
                                clear()
                                print("- Insert a number! -\n")
                                continue
                        
                    elif admchoice == '3':
                        cancel = False
                        clear()
                        
                        if not accounts:
                            print("- There are no accounts yet! -\n")
                            cancel = True
                            
                        if cancel == True:
                            continue
                        
                        while True:
                            print("- Type 'CANCEL' anytime to leave! -\n")
                            print("Insert the number of the account you want to add money to.")
                            moneyid_inp = input(">> ")
                            
                            if moneyid_inp.lower() == 'cancel':
                                clear()
                                cancel = True
                                break
                            
                            try:
                                moneyid = int(moneyid_inp)
                                if moneyid < 1 or moneyid > len(accounts):
                                    clear()
                                    print("- This account number does not exist! -\n")
                                    continue
                                
                                clear()
                                while True:
                                    print("+ Money Panel +\n\n[1] - Add Money\n[2] - Remove Money\n[0] - Quit")
                                    managemoney = input(">> ")
                                    
                                    clear()
                                    if managemoney == '1':
                                        print("Insert the amount of money you wanna add.")
                                        try:
                                            moneyadd = int(input(">> "))
                                            if moneyadd < 0:
                                                clear()
                                                print("- You cannot add a negative amount! -\n")
                                                continue

                                            accounts[moneyid - 1]["money"] += moneyadd

                                            with open(file_path, "w") as f:
                                                json.dump(accounts, f, indent=4)

                                            clear()
                                            print(f"- Added {moneyadd}$ to account number {moneyid} successfully! -\n")
                                            break
                                        except ValueError:
                                            clear()
                                            print("- Insert a valid number! -\n")
                                    elif managemoney == '2':
                                        print("teste")
                                    elif managemoney == '0':
                                        break
                                    else:
                                        print("- Insert an available option! -\n")
                                    
                            except ValueError:
                                clear()
                                print("- Insert a number! -\n")
                                continue
                            
                    elif admchoice == '0':
                        clear()
                        cancel = True
                        break
                    else:
                        clear()
                        print("- Insert an available option! -\n")

                if cancel == True:
                    break

            else:
                clear()
                print("- Incorrect password! -\n")

    elif choice == '0':
        quit()
        break
    else:
        clear()
        print("- Insert an available option! -\n")