# Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.
text = "apple banana apple cherry banana apple"
splited_text=text.split()
print(splited_text)
count={}
for i in splited_text:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)