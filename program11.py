
num = input("Enter a multi-digit number: ")
num = num.strip()
reversed_num = num[::-1]
n1 = int(num)
n2 = int(reversed_num)
if n1 > n2:
    larger = n1
    smaller = n2
else:
    larger = n2
    smaller = n1
