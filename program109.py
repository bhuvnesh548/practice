#age group categorization 
age=int(input("Enter your age: "))
if age < 18:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
if age < 0:
    print("You're not born yet.")
if age > 110:
    print("You're probably dead.")