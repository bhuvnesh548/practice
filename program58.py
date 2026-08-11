#program to print fibonacci series up to n term
nterm=int(input("enter a number"))
a=0
b=1
count=0
while count<nterm:
    fib=a+b
    print(fib)
    a=b
    b=fib
    count+=1
