# Iterate through a given list of numbers and print only those numbers which are divisible by 5.
list=[10, 23, 45, 67, 90, 12, 55, 10, 33, 75, 88, 15, 42, 60, 80, 99, 5, 20, 30, 40, 50, 70, 85, 95, 11, 22, 33, 44, 55, 66, 77, 88, 99]
list2=sorted(list)
for i in list2:
    if i % 5 == 0:
        print(i)