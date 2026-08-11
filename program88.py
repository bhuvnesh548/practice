#pattern 5
for i in range(1, 10):
    for j in range(1,14):
        if i+j==8 or j-i==6 or i-j==2 or i+j==16:
            print("*",end=" ")
        elif i==3 or i==7:
            print("* ",end="")
        else:
            print(" ",end=" ")
    print()


