# Create a program that takes an integer and prints its multiplication table from 1 to 10.
num=int(input("Enter an integer: "))
for i in range(1, 11):
    print(num,"x",i,"=",num*i)