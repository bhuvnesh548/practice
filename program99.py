# Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax
income=int(input("Enter your income: "))
if   income<=10000:
     tax=0
     print("Your tax is:",tax)
elif income<=20000:
     tax=(income-10000)*0.1
     print("Your tax is:",tax)
else:
     print("your tax is:",(income*20)/100)