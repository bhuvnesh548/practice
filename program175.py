#Calculate the total sum of all integers in a list and find the arithmetic mean (average).
def sum(a,b):
    return a+b
def mean(c,d):
    return c/d
list=[10,20,30,40,50]
total=0
nums=len(list)
for i in list:
    total=sum(total,i)
print(total)
print(mean(total,nums))
