import os
os.system("cls")
bank_logo = '''bank of blah blah '''
users = {}
while True:
    print(f"{bank_logo: ^120}")
    choice = int(input("1. Create Account\n2. Login\n3. Exit\nEnter your choice: "))
    match choice:
        case 1:
            print(f"welcome to new account creation. your account no. is {len(users)}")
            name = input("Enter Your name: ")
            account_password = input("Please set your account password: ")
            transection_password = input("please set your transection password: ")
            users[len(users)] = {"money": 200, 
                                 "name": name, 
                                 "account_password": account_password, 
                                 "transection_password": transection_password}
            print("Account created successfully!")
        case 2:
            os.system("cls")
            print(f"{"Log in": ^120}")
            acn = input("Enter your account no.: ")
            print(f"Welcome back, {users[acn]["name"]}")
            print(f"your money: ${users[acn]["money"]}")
        


