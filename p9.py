# program to check if a year is leap year or not 
n=int(input("enter a year "))
if n%4==0 and n%100!=0:
    print("it is a leap year")
else:
    print("it is not a leap year")