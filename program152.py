# Calculate income tax for a given income based on these rules:
# First $10,000: 0% tax
# Next $10,000: 10% tax
# # Remaining income: 20% tax
income=int(input("enter your income "))
if income<=10000:
    tax=0
elif income<=20000:
    tax=(income-10000)*10/100  
else:
    tax=0+((10000*10)/100)
    tax+=(income-20000)*20/100

print("total income tax is : ",tax) 