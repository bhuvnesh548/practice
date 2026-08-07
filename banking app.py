bank_logo = '''bank of blah blah '''
users = {}
while True:
    print(bank_logo)
    choice = int(input("1. Create Account\n2. Login\n3. Exit\nEnter your choice: "))
    match choice:
        case 1: name = input("Enter Your name: ") 

