#Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)
while True:
    add_or_remove=(input("enter the operation : (add/remove)"))
    if add_or_remove=="add":
        fruits.append(input("enter fruit name : "))
        print(fruits)
    elif add_or_remove=="remove":
        fruits.pop(int(input("enter the index no. : ")))
        print(fruits)