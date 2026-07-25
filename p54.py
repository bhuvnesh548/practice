import time
my_time=int(input("enter the time "))
for X in reversed(range(0,my_time)):
    print(X)
    time.sleep(1)
print("time's up ")