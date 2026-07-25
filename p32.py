#Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
num=int(input("enter a number : "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("factorial is ",factorial)
    