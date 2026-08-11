#Take two lists and find the elements that appear in both. Use Sets to perform the operation.
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common_elements=set(list_a)&set(list_b)
print("common Elements are= ",common_elements)