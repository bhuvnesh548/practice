
import os
recipies = {
    "espresso": {"milk": 0, "water": 50, "coffee": 18, "money": 1.5},
    "latte": {"milk": 150, "water": 200, "coffee": 24, "money" : 2.5},
    "capuccino": {"milk": 100, "water":250, "coffee": 24, "money": 3},
    "milk": {"milk": 200, "water": 0, "coffee": 0, "money": 1},
}
resources = {"coffee": 100, "milk":200, "money": 0, "water": 300}
coins = {"penny": 0.01, "nickel":0.05, "dime": 0.1, "quarter": 0.25}
while True:
    for rec in recipies:
        print(f"{rec} - ${recipies[rec]["money"]}")
    choice = input("What do you want? :").lower()
    if choice == "end":
        break;
    elif choice == "resources":
        for r in resources:
            print(f"{r}: {resources[r]}")
    else:
        for ing in resources:
            if ing == "money":
                resources[ing] += recipies[choice][ing]
            else:
                resources[ing] -= recipies[choice][ing]
        print(f"here's your {choice}")

    input("press enter to continue")
    os.system("cls")