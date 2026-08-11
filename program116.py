#programm to find all prime factorials of the number  
num1=input("enter the number ")
num=int(num1)
i=2
while i*i<=num:
    while num%i==0:
        print(i)
        num=num//i
    i+=1
print(num)
