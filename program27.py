#Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
def first_last_same(List_num):
    first_value= List_num[0]
    last_value=List_num[-1]
    if first_value==last_value:
        return True
    else:
        return False

list1=[32,23,54,65,8,6,3,32]
print("result is ", first_last_same(list1))

list2=[22,56,76,45,34,76,32]
print("result is ", first_last_same(list2))
