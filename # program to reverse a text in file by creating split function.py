# program to reverse a text in file 
file=open("1text.txt","r")
text = file.read()
list = []
str = ""
for i in text:
    str += i
    if i == " ":
        list.append(str)
        str = ""
print(list)
reversed_list=list[::-1] 
print(reversed_list)
joinstr=(" ".join(reversed_list))
text2=open("2text.txt","w")
output=text2.write(joinstr)  
file.close() 