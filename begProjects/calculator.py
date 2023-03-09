calc_on = True
continuation = True

def calculation(x,y,symbol):
    if symbol == '-':
        return x - y
    elif symbol == '/':
        return x / y
    elif symbol == '*':
        return x * y
    else:
        return x + y
def user_input():
    num1 = float(input("What is the first number ?\n"))
    num2 = float(input("What is the second number ?\n"))
    operation = input("Press(+) for addition,(-) for subtraction,(/) for division or (*) for multiplication\n")
    return num1,num2,operation
def continue_input(x):
    num2 = float(input("What is the second number ?\n"))
    operation = input("Press(+) for addition,(-) for subtraction,(/) for division or (*) for multiplication\n")
    return x,num2,operation

while calc_on == True:
    inputs = []
    inputs = user_input()
    result = (calculation(inputs[0],inputs[1],inputs[2]))
    print(f"The result is {result}")
    while continuation == True:
        keep_calc = input(f"Do you want to continue with {result} or want to reset?\n")
        if keep_calc == 'continue':
            inputs = []
            inputs = continue_input(result)
            result = calculation(inputs[0],inputs[1],inputs[2])
            print(f"the result is {result}")
        else:
            continuation = False
            calc_on = False