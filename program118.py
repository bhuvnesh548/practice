#programm to find all prime factorials of the number  
num1=int(input("enter the number "))
num=num1
print(num,"= ")
i=2
while i*i<=num+1:
    while num%i==0:      
        print(i,end="")
        num=num//i
        if num>i:
            print(" + ",end="")
    i+=1
if num>i:
    print(num)