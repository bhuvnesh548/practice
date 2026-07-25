#program to find largest among three numbers 
a=int(input("enter the number A "))
b=int(input("enter the number B "))
c=int(input("enter the number C "))
if a>b and a>c:
    print(f"{a} is greatest ")
elif b>a and b>c:
    print(f"{b} is gratest ")
else:
    print(f"{c} is greatest ")