#program to enter a number and reverse it and minus the reverse result untill it is same as original number 
original_number=input("enter a number :")
reversed_number=original_number[::-1]
# for num in original_number:
prenum=0
for i in original_number:
    if i<=str(prenum):
        print(i)
        prenum=i
    print(prenum)
