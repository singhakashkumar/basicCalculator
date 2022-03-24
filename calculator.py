logo = """
 _____________________
|  _________________  |
| | Akash Singh     | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

operators = {
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }



def calculator():
    print(logo)  
    restartCalculator = False
    num1 = float(input("Enter the first number: "))
    for symbol in operators:
            print(symbol)

    while not restartCalculator:
        operator = input("Pick an operator from above: ")
        num2 = float(input("Enter the next number: "))

        result = operators[operator](num1,num2)
        print(f"{num1}{operator}{num2} = {result}")
        condition = input(f"\nType 'y' to continue calculating with {result}, or type 'n' to exit: ")
        if condition == 'y':
            num1 = result
        elif condition == 'n':
            restartCalculator = True
            calculator()

     
calculator()