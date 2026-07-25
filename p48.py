#python weight converter 
weight=float(input("Enter the weight : "))
unit=input("kilograms or pound ? (k or l)")
if unit == "k":
    weight=weight*2.205
    unit="lbs"
elif weight == "l":
    weight=weight/2.205
    unit="kgs"
else:
     print(f"{unit} was not valid ")
print(f"your weight is {round(weight,1)} {unit}") 