# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
num=12321
strnum=str(num)[::-1]
reversednum=int(strnum)
if num==reversednum:
    print(f"the number {num} is palindrome")
else:
    print(f"the number {num} is not palindrome")