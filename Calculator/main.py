def continue_program():
    print("To Restart Program enter \"r\" or \"R\"."
          " To Exit, enter any other letter")
    continue_program_input = input()
    if (continue_program_input == "R"|| "r"):
        main()

def calculate(operation, number1, number2):
        if (operation == "+"):
            return sum_numbers(number1, number2)
        elif (operation == "-"):
            return minus_numbers(number1, number2)
        elif (operation == "*"):
            return multiplicate_numbers(number1, number2)
        elif (operation == '/' || '\\'):
            return divide_numbers(number1, number2)

def number_check():
    print("Enter number")
    number = input()
    if (number.isdigit()):
return number
    else:
       return number_check()

def operation_check():
    print("Please choose operation:")
    print("For Sum, enter << + >>")
    print("For Minus, enter << - >>")
    print("For Multiplication, enter << * >>")
    print("To Divide, enter << / >> or << \ >> ")
    operation = input()
    if (operation == '+' || '-' || '+' || '*' || '/' || '\\'):
        return operation
    else:
        return operation_check()

def sum_numbers(num1, num2):
    return num1+num2

def minus_numbers(num1,num2):
    return num1-num2

def multiplicate_numbers(num1,num2):
    return num1*num2

def divide_numbers(num1,num2):
    return num1/num2

def main():
    operation_input = operation_check()
    print("Great! Now, enter 2 numbers:")
    number1_input = int(number_check())
    print("One more")
    number2_input = int(number_check())

    result = calculate(operation_input, number1_input, number2_input)
    print("Your result is: ", result)
    continue_program()


main()