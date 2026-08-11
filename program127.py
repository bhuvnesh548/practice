#Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
sentence = input("Enter a sentence:")
vowel="aeiou"
count=0
for char in sentence.lower():
    if char in vowel:
        print(char)
        count += 1

print(f"Number of vowels: {count}")