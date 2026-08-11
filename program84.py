#Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.
list1 = [10, 20, 10, 30, 10, 40, 50 ,10 , 10 ]
target = 10
count=0
for i in list1:
    if i == target:
        count+=1
print(f"{target} appear {count} times  ")