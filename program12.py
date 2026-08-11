n=int(input("enter a number : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")
#     for j in range(1,n+1):
#         if j>=(n+1)-i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")
# for i in range(1,n+1): 
#     for j in range(1,n+1):
#         if j>=(n+1)-i:
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print("")
for i in range(1, n + 1): 
    for j in range(1, n-i):
        print(" ", end=" ")
    for k in range(1,i): 
        print(" * ", end=" ")
    print()