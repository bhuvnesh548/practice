# program to reverse a text in file 
file=open("file.txt","r")
text = file.read()
list=text.split()
reversed_list=list[::-1]
joinstr=(" ".join(reversed_list))
text2=open("file2.txt", "w")
input=text2.write(joinstr)  
# print(f"the original text is {text}")
# print(f"the reversed text is {text2}")
file.close()