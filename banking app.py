bank_logo = '''bank of blah blah '''
users = {}
while True:
    print(bank_logo)
    choice = int(input("1. Create Account\n2. Login\n3. Exit\nEnter your choice: "))
    match choice:
        case 1:
            print(f"welcome to new account creation. your account no. is {len(users)}")
            name = input("Enter Your name: ")
            account_password = input("Please set your account password")
            transection_password = input("please set your transection password")
            users[len(users)] = {"name": name, "account_password": account_password, "transection_password": transection_password, "balance": 0}
            print("Account created successfully!")
        


