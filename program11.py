# number=int(input("enter a number "))
# result=0
#while number!=result:
# ascending=sorted(str(number))
# descending=reversed(ascending)
# sorted_number = int("".join(ascending))
# descending=reversed(sorted_number)
# sorted_number = int("".join(descending))

# ascending = int(''.join(sorted(number)))
# descending = int(''.join(sorted(number, reverse=True)))
# print(f"the number in ascending order is {ascending}")
# print(f"the number in descending order is {descending}")
# subtract=descending-ascending
# print(subtract)
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
