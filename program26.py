#Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
numbers=[1,3,5,7,9,9,4,3,6,7,9,8,6,4,3,2,3,5,7,6]
uniquelist=list(set(numbers))
print("the new list is ",uniquelist)