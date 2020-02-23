def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def more_calculating():
    keep_going = input("Would you like to do more calculating (yes or no)?:")
    if keep_going == "yes" or keep_going == "Yes" or keep_going == "Y" or keep_going == "y":
        main()
    else:
        print("Thank you for using my calculator.")


def main():
    operation = input("What do you want to do (+,-,*,/):")
    if operation != "+" and operation != "-" and operation != "*" and operation != "/":
        print("You must enter a valid operation")
        main()
    else:
        valid_input = False
        while not valid_input:
            try:
                num1 = float(input("Enter num1:"))
                num2 = float(input("Enter num2:"))
                valid_input = True
            except:
                print("you must enter numbers.")
        if operation == "+":
            print(add(num1, num2))
            more_calculating()
        elif operation == "-":
            print(subtract(num1, num2))
            more_calculating()
        elif operation == "*":
            print(multiply(num1, num2))
            more_calculating()
        elif operation == "/":
            print(divide(num1, num2))
            more_calculating()


main()
