# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
values = input("Enter comma-separated numbers: ")
# Split the input string into a list
number_list = values.split(',')
# Create a tuple from the list
number_tuple = tuple(number_list)
# Print the list and tuple
print(number_list)
print(number_tuple)
