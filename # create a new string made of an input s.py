# create a new string made of an input string’s first, middle, and last characters.
string=input("enter a string : ")
first=string[0]
middle=len(string)//2
mid=string[middle]
last=string[-1]
print(f"{first}{mid}{last}")