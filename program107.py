import math
num1 = 60
num=num1
j=[]
i = 2
num2=math.sqrt(i)
while num2<= num1:
    while num1 % i == 0:
        j.append(i)
        num1= num1//i
    i += 1
factors=" ".join(str(j))
print(factors,)
