#Iterate through a given list of numbers and print only those numbers which are divisible by 5
num_list=[12,15,20,35,21,23,45,64,50]
print(f"the given list is {num_list}")
print("divisible by 5 :")
for num in num_list:
    if num%5==0:
        print(num)