#python compound intrest calculator 
principle=int(input("enter the principle amount:"))
rate=float(input("enter the rate of intrest %: "))
time=int(input("enter the time "))
total=principle*pow ((1+rate/100),time)
print(f"balance after {time} year is {total} ")
