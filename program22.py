#Write a Python program that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, 
# return their product; otherwise, return their sum.
num1=int(input("enter the 1st number : "))
num2=int(input("enter the 2nd number : "))
product=num1*num2
sum=num2+num1
if product<=1000:
    print(f"the product of {num1} and {num2} is {product}")
else:
    print(f"the sum of {num1} and {num2} is {sum}") 