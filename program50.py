#shopping cart program 
items=[]
prices=[]
total=0
while True:
    items=input("enter the item(press q and enter to exit) :")
    if items.lower=="q":
        break
    else:
        price=float(input("enter the price : "))
        items.append(items)
        prices.append(price)
print("your cart ")
for i in items:
    print(items)
print(items)