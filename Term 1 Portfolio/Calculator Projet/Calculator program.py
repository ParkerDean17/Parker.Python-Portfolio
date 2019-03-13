#Parker Dean
#10/3/18
#Calculator program

def add(num1, num2):
    addition = num1 + num2
    return addition

def subtract(num1, num2):
    subtraction = num1 - num2
    return subtraction

def multiply(num1, num2):
    multiplication = num1 * num2
    return multiplication

def divide(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if num1 != 0:
        division = num2 / num1
        return division
    else:
        return 0

def remainder(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if num1 != 0:
        remainder = num2 % num1
        return remainder
    else:
        return 0

def display_output(message):
    print(message)

def get_input(message):
    varval = input(message)
    return varval

def get_int_input(message):
    var_value = input(message)
    if var_value.isdigit():
        var_value = int(var_value)
        return var_value
    else:
        display_output("that wasn't a number")
        det_int_input(message)

def check_math(test_value, operator, num1, num2):
    if operator == "+":
        checked_value = num1 + num2

    elif operator == "-":
        checked_value = num1 - num2

    elif operator == "*":
        checked_value = num1 * num2

    elif operator == "/":
        num1 = float(num1)
        num2 = float(num2)
        if num1 != 0:
            checked_value =  num1/num2
        else:
            checked_value = 0
            
    elif operator =="%":
        num1 = float(num1)
        num2 = float(num2)
        if num1 != 0:
            checked_value =  num1%num2
        else:
            checked_value = 0

    if checked_value ==test_value:
            checked = True
            print(checked_value)
    else:
            checked = False
            print(checked_value)
    return checked
                

def main():
    num1 = get_int_input("please enter a number: ")
    num2 = get_int_input("please enter a number: ")
    operator = get_input("What is your operation?  Enter + - * / or % only. ")

    if operator == "+":
        test_value = add(num1,num2)
    elif operator == "-":
        test_value = subtract(num1,num2)
    elif operator == "*":
        test_value = multiply(num1,num2)
    elif operator == "/":
        num1 = float(num1)
        num2 = float(num2)
        test_value = divide(num2,num1)
    elif operator == "%":
        num1 = float(num1)
        num2 = float(num2)
        test_value == remainder(num1, num2)
    else:
        display_output("This is not a valid operation")
    if check_math(test_value, operator, num1, num2):
        display_output("after a second check the correct answer is " + str(test_value))
    else:
        display_output("something in the calculation was wrong try it again.")
        print(test_value)
        
        main()

main()



    



