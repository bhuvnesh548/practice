"""Write a program to check if a number is an Armstrong number. 
An Armstrong number (for a 3-digit number) is an integer 
such that the sum of the cubes of its digits is equal to the number itself 
(e.g., 153 = 1^3 + 5^3 + 3^3)."""
num=153
cube_sum = sum(int(digit) ** 3 for digit in str(num))
if num == cube_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")