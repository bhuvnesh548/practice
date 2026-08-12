# Write a single-line list comprehension that takes a list of strings, 
# filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
def newlist(list):
    newlsit=[]
    for i in list:
        if len(i)>=4:
            print(i.upper())
            newlsit.append(i.upper())
    return newlsit
words = ["apple", "bat", "cherry", "dog", "elderberry"]
print(newlist(words))
    