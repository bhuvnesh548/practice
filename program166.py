# Given a list of integers, move all even numbers to the beginning of the list and all odd numbers to the end.
list=[1, 2, 3, 4, 5, 6]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even + odd)