# Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.
sentance="the quick brown fox jumps over the lazy dog "
vowel=""
consonent=""
for i in sentance.lower():
    if i in "aeiou":
        vowel+=i
    elif i!=" ":
        consonent+=i
print(f"{vowel=}")
print(f"{consonent=}")
print(f"there are {len(vowel)} vowels and {len(consonent)} consonent in the {sentance=}")
