str=("my name is bhuvnesh ")
words = []
word = ""
for i in str:
    word += i
    if i == " ":
        words.append(word)
        word = ""
print(words)