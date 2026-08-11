# Write a program to create a new string made of the middle three characters of an input string of odd length.
string=input("enter a string :")
mid=len(string)//2
print(f"{string[mid-1]}{string[mid]}{string[mid+1]}")
