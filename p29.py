#Iterate through the first 10 numbers (0–9). 
# In each iteration, print the current number, the previous number, and their sum.
n=int(input("enter a number "))
prenum=0
for i in range(n):
    sum=i+prenum
    print(f"the sum of previous number {prenum} and current number {i} is {sum}")
    prenum=i