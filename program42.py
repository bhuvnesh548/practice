#Write a function to remove characters from a string starting from index 0 up to n and return a new string.
def substring(string,n):
    print("original string is ",string)
    res=string[n:]
    return res
print(substring("bhuvnesh",3))
