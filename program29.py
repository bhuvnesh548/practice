# Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in list1:
    if list1[0] == list1[-1]:
        print(True)
    else:
        print(False)