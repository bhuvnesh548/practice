# Given a nested list (a list containing other lists), 
# write a program to “flatten” it into a single list containing all the individual elements.
def flatten(nestlist):
    newlist=[]
    for i in nestlist:
        for j in i:
            newlist.append(j)
    return newlist

nested_list = [[10, 20], [30, 40], [50, 60]]
print(flatten(nested_list))