# Functions with Outputs


# Calculator

def calculate(num1, operation, num2):
    """Does simple math"""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == 'x':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    
print("Welcome to the calculator app!")

first_number = float(input("What is the first number?"))
oper = input("What operation would you like to perform?\n + \n - \n x \n /")
second_number = float(input("What is the second_number?"))
result = calculate(first_number, oper, second_number)
print(f"The result of your calculation is {result}")
restart = input(f"If you would like to continue operating with {result}, type 'y'. To begin again, type 'n'.")

while restart == 'y':
    first_number = result
    oper = input("What operation would you like to perform?\n + \n - \n x \n /")
    second_number = float(input("What is the second_number?"))
    result = calculate(first_number, oper, second_number)
    print(f"The result of your calculation is {result}")
    restart = input(f"If you would like to continue operating with {result}, type 'y'. To begin again, type 'n'.")
