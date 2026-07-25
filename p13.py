#program to print all prime numbers between a interval 
a=int(input("enter the lower limit "))
b=int(input("enter the upper limit "))
for num in range(a,b):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)