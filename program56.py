# Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.
numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
even=[]
odd=[]
for each_element in numbers:
    if each_element%2==0:
        odd.append(each_element)
    else:
        even.append(each_element)
print("even nums = ",even)
print("odd nums = ",odd)