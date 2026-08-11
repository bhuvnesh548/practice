#program to enter a number and reverse it and subtract the reverse result untill it is same as original number 
original_number=input("enter a number :")
reversed_number=original_number[::-1]
print(f"reversed number is {reversed_number}")
for i in original_number:
    if original_number!=reversed_number:
        Subtract=int(original_number)-int(reversed_number)
        original_number=Subtract
        print(Subtract)
        