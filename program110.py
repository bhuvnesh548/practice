import random 
from docx import Document
doc= Document()
rows=12
colums=19
print("   ",end="") 
g=random.randint(1,13) 
print(g,end=" ")
print()
for i in range(1,colums+1):
    f=random.randint(1,19)
    print(f)