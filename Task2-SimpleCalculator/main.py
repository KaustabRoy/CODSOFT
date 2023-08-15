# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.

from termcolor import colored

class FormatInput:

    def __init__(self):
        self.expression = input(colored("Enter expression in pattern 'num_1 operator num_2': ", "cyan"))

    def format_exp(self):
        exp = self.expression.split(" ")
        try:
            val1 = float(exp[0])
            oper = exp[1]
            val2 = float(exp[2])
            return val1, val2, oper
        except ValueError:
            print(colored("Got anything other than numbers!", 'red'))

class Calculator:

    def __init__(self, in_num1, in_num2, op_choice):
        self.num1 = in_num1
        self.num2 = in_num2
        self.choice = op_choice
        self.result = 0

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return colored("Division by Zero not possible !", "yellow")

    def operation(self):
        if self.choice == '+':
            self.result = self.add()
        elif self.choice == '-':
            self.result = self.subtract()
        elif self.choice == '*' or self.choice == 'x':
            self.result = self.multiply()
        elif self.choice == '/':
            self.result = self.divide()
        else:
            self.result = colored("Invalid operator choice !!", "red")
        return self.result

if __name__ == '__main__':
    while True:
        user_input = FormatInput()
        try:
            num1, num2, op = user_input.format_exp()
            print(colored(f"First Number = {num1}\nOperator = {op}\nSecond Number = {num2}", "magenta"))
            calc = Calculator(num1, num2, op)
            result = calc.operation()
            print(colored(f"{num1} {op} {num2} = {result}", "blue"))
        except TypeError:
            print(colored("Please enter numbers and try again!", "light_yellow"))
        finally:
            in_end = input("Do you want to continue calculation(Y|y): ")
            if in_end.lower() == 'y':
                continue
            else:
                break