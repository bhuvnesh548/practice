# Write a program to calculate the sum of the series 2 + 22 + 222 + 2222 + …. up to N terms. 
# For example, if n=5, the series is 2 + 22 + 222 + 2222 + 22222.
num=5
n2=""
for i in range(1,num+1): 
    n2+="2"*i
    n2+=" "
striped=n2.strip()
print(f"{striped.replace(" ","+")}")