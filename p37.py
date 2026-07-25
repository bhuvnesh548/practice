#Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
print("printing current and previous number in the range 1 to n")
num=int(input("enter a number : "))
previous_num=0
for i in range(0,num):
    sum=previous_num+i
    print(f"the sum of previous number {previous_num} and current number {i} is {sum}")
    previous_num=i