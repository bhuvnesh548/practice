#Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
num=int(input("enter a number :"))
prenum=0
for i in range(1,num+1):
    sum=prenum+i
    print(f"previous number {prenum}  current number {i}  =    {sum}")
    prenum=i
