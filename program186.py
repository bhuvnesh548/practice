# Create a function func1() such that it can accept a variable number of arguments and print all of them. Whether you pass two numbers or five, the function should handle them all without error
def func1(list):
    for i in list:
        print(i)

func1([20, 40, 60])
func1([80, 100])