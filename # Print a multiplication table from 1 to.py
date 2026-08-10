# Print a multiplication table from 1 to 10 in a formatted grid.
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print()
    