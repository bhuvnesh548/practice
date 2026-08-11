#program of table 
import random 
rows=12
col=19
row1=[]
col1=[]
while len(row1)<rows:
    g=random.randint(1,12)
    if g not in row1:
        row1.append(g)
while len(col1)<col:
    f=random.randint(1,19)
    while f not in col1:
        col1.append(f)
print("  ",end="")
for i in row1:
    if i>=10:
        print(i,end=" ")
    else:
        print(i,end=" ")
print()
for i in col1:
    if i>=10:
        print( i)
    else:
        print(i)
