import math
num=int(input("enter a number : "))
num1 = num
i = 2
num2=math.sqrt(i)
while num2<= num1:
    if num1 % i == 0:
        print(i)
        num1= num1//i
    i += 1

print(num1),
print(num)