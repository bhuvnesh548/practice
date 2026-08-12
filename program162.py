"""The Collatz conjecture states that if you start with any positive integer n,
and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. 
Repeat the process. The sequence will always eventually reach 1. 
Write a program to print this sequence for a given number."""
n=6
for i in range(n):
    if n <= 0:
        print("Please enter a positive integer.")
        break
    print(n, end=' ')
    if n == 1:
        break
    elif n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1