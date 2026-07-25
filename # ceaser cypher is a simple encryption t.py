# ceaser cypher is a simple encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3, 'A' would become 'D', 'B' would become 'E', and so on. 
# This program implements a simple Caesar cipher encryption and decryption.
message ="zebra"
shift =3
letters ="abcdefghijklmnopqrstuvwxyz"
encrypted_message =""
for i in message.lower():
    if i in letters:
        index =letters.index(i)
        new_index =(index + shift) % 26
        encrypted_message +=letters[new_index]
print("Encrypted message:",encrypted_message)
