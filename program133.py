#hangman Game 
import random 
words=["mango","apple","grape","car","honey","computer","house","mouse"]
word=random.choice(words)
print(word)
out=False 
word_placed=""
while not out:
    letter=input("guess a letter : ").lower()
    for i in word:
        if i==letter:
            word_placed+=i
        else:
            word_placed+="-"
    if "-" not in word_placed:
        out=True
        print("you won")
    print(word_placed)
