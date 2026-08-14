from csv import*
print("0-name\n1-surname\n2-email\n3-Phone\n4-city")
n=int(input("enter a number "))
list=[]
list2=[]
with open("data.csv","r") as f:
    data= reader(f)
    for row in data:
        for i in row:
            if i==row[n]:
                list2.append(i)
print(list2)