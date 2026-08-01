# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
def fact(x):
    factorial=1
    for i in range(1,x+1):
        fact=i*factorial
        factorial=fact
num=int(input("enter a number : "))
print(fact(num))

