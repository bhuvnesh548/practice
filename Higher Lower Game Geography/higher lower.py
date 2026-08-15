import random, os;
from countries import data;
has_lost = False;
categories = ["area", "neighbouring countries", "highest point", "population"]
cat = random.choice(categories)
lComp = random.sample(list(data), 2)
print(lComp);
a = lComp[0]
b = lComp[1]
score = 0
while not has_lost:
    os.system("cls")
    print(f"Compare:\n{a}, a country in {data[a]["continent"]}, has ", end = "")
    if cat == "neighbouring countries":
        print(f"{data[a][cat]} {cat}")
    elif cat == "highest point":
        print(f" a {cat} of {data[a][cat]} metres")
    elif cat == "population":
        print(f" a {cat} of {data[a][cat]} millon")
    elif cat == "area":
        print(f" an {cat} of {data[a][cat]} km²\n")

    print("Vs.\n")
    choice = input(f"{b}, a country in {data[b]["continent"]} \n\ndoes {b} have higher or lower {cat} than {a}? : ").lower();


    if data[a][cat] > data[b][cat]:
        if choice.startswith('l'):
            has_won = True
        else: has_won = False

    elif data[a][cat] < data[b][cat]:
        if choice.startswith('h'):
            has_won = True;
        else: has_won = False

    else:
        has_won = True;
    
    if has_won == True:
        score += 1;
        print(f"you won!\n{a}: {data[a][cat]}\n{b}: {data[b][cat]}\nyour score: {score}")
        a = b;
        b = random.choice(list(data))
        
    else:
        print(f"you lost\n{a}: {data[a][cat]}\n{b}: {data[b][cat]}\nyour score: {score}")
        has_lost = True
    input("Press <ENTER> to continue.")

