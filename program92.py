import random

crock = "👊"
cpaper = "✋" 
cscissors = "✌️"
choices = [crock, cpaper, cscissors]
bot_score = 0
user_score = 0
bestof = int(input("Welcome to Stone Paper Scissors Bot\nPlay match best of: "))
while True:
    user_choice = int(input("Enter 0 for 👊, 1 for ✋ and 2 for ✌️\n"))
    bot_choice = random.randint(0,2)
    print(f"Your choice: {choices[user_choice]}\n")
    print(f"Bot's choice: {choices[bot_choice]}\n")
    if (bot_choice == 0 and user_choice == 2) or(bot_choice == 1 and user_choice == 0) or (bot_choice == 2 and user_choice == 1):
        bot_score += 1
        print(f"You lost. \nbot: {bot_score}\nYou: {user_score}")
    elif (bot_choice == user_choice):
        print(f"draw \nbot: {bot_score}\nYou: {user_score}")
    else:
        user_score += 1
        print(f"You won!. \nbot: {bot_score}\nYou: {user_score}")
    if user_score + bot_score == bestof:
        if bot_score > user_score:
            winner = "Bot"
        elif bot_score == user_score:
            winner = "Nobody"
        else:
            winner = "You"
        print(f"Game Over: {winner} won.\nstats:\nbot: {bot_score}\nYou: {user_score}")
        break