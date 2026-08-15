import getpass
username =input("enter username :")
pwd=getpass.getpass("enter password :")
if username=="bhuvnesh" and int(pwd)==123 :
    print("login successful")
else:
    print("Login Failed!")