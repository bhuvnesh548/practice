#create a program that accept the number from the user and print all factors of a number 
while True:
    n=int(input("enter a number : "))
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)    
    print(factors)
