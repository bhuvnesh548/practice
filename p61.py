#program to generate and print a random number 
import random
num1=random.randint(100000,999999)
num2=random.randint(100000,999999)
if num1>num2:
    print(num1,"-",num2,"=")
else:
    print(num1,"+",num2,"=")