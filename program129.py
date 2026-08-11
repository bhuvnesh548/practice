# Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
num1, num2 = 0, 1
print("Fibonacci series:")

for i in range(15):
    print(num1, end="  ")
    # Calculate next term
    res = num1 + num2
    # Update values for next iteration
    num1 = num2
    num2 = res