# Write a program to remove all duplicate values from a list using a loop, maintaining the original order of elements.
list=[1, 2, 2, 3, 4, 4, 4, 5]
newlist=[]
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)