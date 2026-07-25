# treasure hunt 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction =input ("choose where you want to go left or right direction : ")
if direction.lower()=="left":
    print("oh noooo ! there is a lion ,you loose !")
elif direction.lower()=="right":
    print("congrats! now you reached at the riverbank.")
    choice=input("do you want to wait for a ""boat"" or ""swim"" to cross the river ")
    if choice.lower()=="swim":
        print("You get captivated by the songs of sirens and lured down to the lake and drown. Game Over.")
    elif choice.lower()=="boat":
        doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if doors.lower() == "blue":
      print("You enter a room of of puppies. You are immobilized by cuteness. You win their love, but lose the treasure. Game Over.")
    elif doors.lower() == "yellow":
      print("You found the treasure! You Win!")
    elif doors.lower() == "red":
      print("You enter a room full of doors to other rooms and cannot escape. Game Over.")
    else: 
      print("You chose a door that doesn't exist. Game Over.")
