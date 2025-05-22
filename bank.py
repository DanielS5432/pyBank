import os

def clear():
    os.system("cls")

def quit():
    clear()
    print("- Goodbye! -\n")

adminPass = "Admin123"

while True:
    print("\n+ Welcome to pyBank! +\n\n[1] - Log In\n[2] - Sign Up\n[3] - Admin Panel\n[0] - Quit")
    choice = input(">> ")

    if choice == '1':
        clear()
        print("wip")
    elif choice == '2':
        clear()
        print("wip")
    elif choice == '0':
        quit()
        break
    else:
        clear()
        print("- Insert an available option! -")