from time import sleep
from os import system
def lst2str(lst):
    str = ""
    for i in lst:
        str += i 
    return str
def typewrite(str, speed):
    from time import sleep
    for char in str:
        print(char, end="")
        sleep(speed/100)
def typedel(str, speed):
    lst = list(str)
    for i in str:
        print(lst2str(lst))
        del(lst[-1])
        sleep(speed/100)
        system("cls")



typewrite('''Lorem ipsum dolor sit amet consectetur 
adipisicing elit. Corporis neque perspiciatis non consequatur,
esse fugiat architecto enim. Inventore quas quos, expedita suscipit incidunt,
facere est mollitia nemo quidem quaerat distinctio.
Lorem ipsum dolor sit amet consectetur adipisicing elit.
Corporis neque perspiciatis non consequatur, esse fugiat architecto enim. 
Inventore quas quos, expedita suscipit incidunt,
 facere est mollitia nemo quidem quaerat distinctio.Lorem ipsum 
dolor sit amet consectetur adipisicing elit. Corporis neque
perspiciatis non consequatur, esse fugiat architecto enim.
Inventore quas quos, expedita 
suscipit incidunt, facere est mollitia nemo quidem quaerat distinctio.''', 3)
system("cls")
typedel('''Lorem ipsum dolor sit amet consectetur 
adipisicing elit. Corporis neque perspiciatis non consequatur,
esse fugiat architecto enim. Inventore quas quos, expedita suscipit incidunt,
facere est mollitia nemo quidem quaerat distinctio.
Lorem ipsum dolor sit amet consectetur adipisicing elit.
Corporis neque perspiciatis non consequatur, esse fugiat architecto enim. 
Inventore quas quos, expedita suscipit incidunt,
 facere est mollitia nemo quidem quaerat distinctio.Lorem ipsum 
dolor sit amet consectetur adipisicing elit. Corporis neque
perspiciatis non consequatur, esse fugiat architecto enim.
Inventore quas quos, expedita 
suscipit incidunt, facere est mollitia nemo quidem quaerat distinctio.''', 3)
