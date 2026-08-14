# Identify the largest and smallest numerical values within a provided list.
def minmax(list):
    max=0
    min=0    
    for i in list:
        if i>max:
            max=i
        else:
            min=i
    print(f"{min=}")
    print(f"{max=}")
list=[21,65,35,93,76,10,32,65,32,123]
minmax(list)