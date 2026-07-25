#Display only those characters which are present at an even index number in given string.
string=input("enter a string :")
print("the original string is ",string )
even=string[0::2]
print("even index numbers in string are ",even)

#2nd method
print("")
print("")

size=len(string)
print("printing only string even characters ")
for i in range(0,size,2):
    print("index[",i,"]",string[i])