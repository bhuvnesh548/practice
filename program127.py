#Write a program to create a new string made of an input string’s first, middle, and last characters.
str1 = "bhuvnesh"
print("Original String is", str1)
first_char = str1[0]

res = len(str1)
middle_index = int(res / 2)
mid_char = str1[middle_index]
last_char = str1[-1]

res_str = first_char + mid_char + last_char
print("New String:", res_str)
