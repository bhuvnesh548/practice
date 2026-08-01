# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
def dictionary(number):
    dictionary={}
    for i in range(1,number+1):
        square=i*i
        dictionary[i]=square
    return dictionary
num=int(input("enter a number : "))
print(dictionary(num))
