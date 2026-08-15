# Read an existing file test.txt and store every line as an individual element in a Python list.
list=[]
with open("data.csv","r")as f:
    for i in f:
        list=[]
        list.append(i)
        print(list)
