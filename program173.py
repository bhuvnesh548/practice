# Take a given list and modify it through five specific actions:

# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.
list= [100, 50, 400, 500]
print(f"original list={list}")
list[2]=600
print(f"changed list={list}")
list.insert(1,300)
print(f"insert={list}")
list.remove(600)
print(f"remove={list}")
list.pop(0)
print(f"popped={list}")