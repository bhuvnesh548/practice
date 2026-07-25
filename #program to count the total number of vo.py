#program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
sentence=input("enter a sentence : \n")
vowel="aeiou"
count=0
for char in sentence.lower():
    if char in  vowel:
        count+=1
print(count)