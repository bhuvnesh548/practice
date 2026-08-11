# Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.
with open('#Anotes.txt', 'w') as file:
    file.write("This is the first line of text.\n")
    file.write("This is the second line of text.\n")
    file.write("This is the third line of text.\n")

with open('#Anotes.txt', 'r') as file:
    contents = file.read()
    print(contents)
