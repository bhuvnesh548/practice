#Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.
text = "hello world from python"
split=text.split()
capitalize=[]
for i in split:
    cap=i.capitalize()
    capitalize.append(cap)
joine=" ".join(capitalize)
print(joine)
    
