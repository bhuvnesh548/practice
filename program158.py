#email slicer 
email=input("enter your email : ")
if ".com" in email and "@" in email:
    index=email.index("@")
    username=email[:index]
    domain=email[index:]
    print(f"your username is {username} and domain is {domain}")
else: 
    print("enter a valid email")