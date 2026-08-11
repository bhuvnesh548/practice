# Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.
list1=[45,44,76,62,54,13,23,58,59,54]
list2=[95,67,12,56,84,98,89,57,97,22]
odd=[]
even=[]
for i in list1:
    if i%2==0:
        odd.append(i)
for i in list2:
    if i%2!=0:
        even.append(i)
print("odd=",odd)
print("even=",even)