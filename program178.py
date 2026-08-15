# You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these as a table with aligned columns.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'name':<10}{'scores'}")
print(f"-"*15)
for i,j in zip(names,scores):
    print(f"{i:<12}{j}")
    