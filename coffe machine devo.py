import os
def format_us_currency(money):
    cents = int((money % 1) * 100)
    dollars = money // 1
    return [dollars, cents]
def take_payment():
    total_payment = 0
    for coin in coins:
        payment = int(input(f"How many {coin}s are you paying? : "))
        total_payment += (payment * coins[coin])
    change = total_payment - recipies[choice]["money"]
    if change > 0:
        print(f"You payed ${total_payment} for a beverage that costs only ${recipies[choice]["money"]}. Here is your {format_us_currency(change)[0]} dollars and {format_us_currency(change)[1]} cents of change.")
    elif change < 0:
        print(f"not enough money. price of {choice}: ${recipies[choice]["money"]}")
        return False
    return True
def add():
    for ing in resources:
        if ing != 'money':
            amt = int(input(f"how much {ing} do you want to add?"))
            resources[ing] += amt  
def report():
    for r in resources:
        print(f"{r}: {resources[r]}", end="")
        if r == 'milk' or r == 'water':
            print("ml")
        elif r == 'coffee': print("g")
        else: print("dollars")
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
        print(f"{rec} - ${recipies[rec]["money"]}")#print menu
    choice = input("What do you want? : ").lower()# take user's input
    if choice == "oper/->off":
        break;#get out of the while loop and the program
       
    elif choice == "oper/->resources" or choice == 'oper/->report':
        report()#print the resources (run the report() function (see above on line ))

    elif choice.startswith('nothing'): print("well, then goodbye! visit sometime. there's some good coffee in there.")

    elif choice in recipies:
        print("please pay $", recipies[choice]["money"] )
        payment_was_successful = take_payment();
        for ing in resources:
            if ing == "money":
                resources[ing] += recipies[choice][ing]
            else:
                if resources[ing] - recipies[choice][ing] < 0:
                    print(f"Not enough {ing}.")
                else:
                    resources[ing] -= recipies[choice][ing];
        if payment_was_successful:
            print(f"here's your {choice}")

    else: print(f"{choice} is not a beverage we sell.")



    input("press enter to continue")
    os.system("cls")