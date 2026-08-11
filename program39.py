#temprature converter
temprature=float(input("enter the temprature "))
unit=input("is this temprature is in farenheit or celsius : (C/F)")
if unit=="c":
    temprature=((temprature*9)/5)+32
    print(f"the temprature in farenheit is {temprature}")
elif unit=="f":
    temprature=(temprature-32)*5/9
    print(f"the temprature in celsius is {temprature}")
else:
    print(f"{unit} is invalid")