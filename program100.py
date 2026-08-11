def add(number_1, number_2):
    return number_1 + number_2;
def subtract(number_1, number_2):
    return number_1 - number_2;
def multiply(number_1, number_2):
    return number_1 * number_2;
def divide(dividend, divisor):
    return dividend / divisor;
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              "×":multiply,
              "÷": divide,
              }
choice = "n";
while choice != "q":
    if(choice == "n"):
        number_1 = float(input("Enter the first number: ")) 
        operator = input("Pick an operation: addition, subtraction, multiplication or division. : ")
        number_2 = float(input("Enter the second number: ")) 
        ans = operations[operator](number_1, number_2)
        print(f"{number_1} {operator} {number_2} = {ans}")
    elif(choice == "c"):
        number_1 = ans;
        operator = input(f"Pick an operation to do with {number_1}: addition, subtraction, multiplication or division. : ")
        number_2 = float(input("Enter the second number: ")) 
        ans = operations[operator](number_1, number_2)
        print(f"{number_1} {operator} {number_2} = {ans}")
    elif(choice == "q"):
        break;
    else:
        print(f"{choice} is not a valid choice.");
    choice = input(f"Enter;\n'c' to continue doing operations with {ans}\n'n'to do a new calculation\n'q' to quit program\nyour choice: ").lower();




