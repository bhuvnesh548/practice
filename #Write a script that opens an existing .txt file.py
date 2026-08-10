# Write a script that opens an existing .txt file and counts the total number of words it contains.
with open('#Anotes.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print(f'The total number of words in the file is: {word_count}')