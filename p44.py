#Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
num=input("enter a number you want to check if it is palindrome or not : ")
original_number=num
reversed_number=num[::-1]
if original_number==reversed_number:
    print(f"the number {num} is palindrome ")
else:
    print("the number is not palindrome")