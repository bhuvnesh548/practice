#program to enter a number and reverse it and minus the sorted reverse result untill it is same as original number 
original_number=int(input("enter a number :"))
print(original_number)
reversed_number=str(original_number[::-1])
sorted_list=sorted([original_number]) 
print(sorted_list)
