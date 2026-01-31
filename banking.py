# the banking system
import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

accounts = {}

def createAccount():
    # clear_screen()
    acc_no = random.randint(1000, 2000)
    balence = 0
    if acc_no in accounts:
        print("Account already Exists")
        return
    
    name  = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    contactNo = input("Enter Your Contact No: ")
    address = input("Enter Your Address: ")
    password = input("Set Password: ").strip()
    
    accounts[acc_no] = {
        "name" : name,
        "email" : email,
        "contact": contactNo,
        "address" : address,
        "password" : password,
        "balence" : balence
    }
    
    print("Processing...")

    time.sleep(2)
    print("Your Account is Successfully Created...\n")
    print("Your Details are: \n") 
    print("Account ID: {} \nName: {} \nEmail: {} \nPassword {} \nContact: {} \nAddress: {}".format(acc_no, name,email, password, contactNo, address))

    time.sleep(5)

def loginAccount():
    while True:
        
        account_no = int(input("Enter Your Account ID: "))
        password = input("Enter Your Password: ").strip()
        if account_no in accounts:
            if accounts[account_no]['password'] == password:
                print("Processing...")
                time.sleep(3)
                print("Loggedin successfully\n")
                bankMenu(account_no)
                break
            else:
                print("Processing...")
                time.sleep(3)
                print("Incorrect password\n")
                continue
        else:
            print("Processing...")
            time.sleep(3)
            print("Account not Found...!")
    clear_screen()
        
                
       
       
def depositeMoney(acc_no):
    clear_screen()
    amount = int(input("Amount: "))
    
    if amount > 0:
        accounts[acc_no]["balence"] += amount
        print("{} RS Deposite Successfully".format(amount))
        print(f"New Account Balance is : {accounts[acc_no]['balence']}")
    else:
        print(f"{amount} RS can't be Deposite...")
    
def withdrawMoney(acc_no):
    clear_screen()
    amount = int(input("Enter Amount: "))
    
    if amount <= accounts[acc_no]['balence']: 
        accounts[acc_no]['balence'] -= amount
        print("Get your cash____")
        print("You have successfully withdraw {} RS".format(amount))
        print(f"Remaining Balence is {accounts[acc_no]['balence']}")
    else:
        print("Insufficient Balance, you only have ", accounts[acc_no]['balence'], " RS...")
        
    
def checkBalence(acc_no):
    print(f"{accounts[acc_no]['name']}! You have {accounts[acc_no]['balence']} RS")
    

def details(acc_no):
    clear_screen()
    print("\n---Account Information---")
    print(f"Account ID: {acc_no}")
    print(f"Name: {accounts[acc_no]['name']}")
    print(f"Email: {accounts[acc_no]['email']}")
    print(f"Contact: {accounts[acc_no]['contact']}")
    print(f"Balence: {accounts[acc_no]['balence']} RS\n")
    
    
    
        
def bankMenu(acc_no):
    
    while True:
        
        print("\n---user menu---")
        print("1. Deposite Money")
        print("2. Withdraw Money")
        print("3. Check Balence")
        print("4. Check Account Details")
        print("5. Exit\n")
        
        user = int(input("Enter Your Choice: "))
        
        if user == 1:
            depositeMoney(acc_no)
        elif user == 2:
            withdrawMoney(acc_no)
        elif user ==3 :
            checkBalence(acc_no)
        elif user == 4:
            details(acc_no)
        elif user == 5:
            print("Thank You...")
            break
        else:
            print("Invalid Typed\n")
            continue
        
        

def displayMenu():
    
    while True:
    
        print("----Welcome to Banking System----".center(80, ' '))
        print("1. Create Account")
        print("2. Login Account")
        print("3. Exit")
        user = int(input("Enter a choice: "))
        if user == 1:
            createAccount()
        elif user == 2:
            loginAccount()
        elif user == 3:
            print("Thank You!!!")
            break
        else:
            print("Invalid Number\nTry Again...")
            continue

if __name__ == "__main__":
    displayMenu()

