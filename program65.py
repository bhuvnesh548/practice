#pattern 5
for i in range(1, 10):
    for j in range(1,14):
        if i+j==8:
            print("*",end=" ")
        elif j-i==6:
            print("*",end=" ")
        elif i-j==2:
            print("*",end=" ")
        elif i+j==16:
            print("*",end=" ")
        elif i==3:
            print("* ",end=" ")
        elif i==7:
            print("*",end=" ")
    print()


