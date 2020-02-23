roll = input("Would you like to roll a dice?")
if roll == "yes" or roll == "Yes" or roll == "Y" or roll == "y":
    sides_defined = False
    while not sides_defined:
        try:
            sides = int(input("How many sides would you like the die to have?"))
            if sides >= 1:
                sides_defined = True
            else:
                print("you can't enter a value lower than one.")
        except ValueError:
            print("You must enter an integer value for how many sides the die has.")
    while roll == "yes" or roll == "Yes" or roll == "Y" or roll == "y":
        try:
            number_of_dice = int(input("How many dice would you like to roll?"))
            import random

            for x in range(number_of_dice):
                print(random.randint(1, sides))
            roll = input("Would you like to roll more dice?")
        except ValueError:
            print("You must enter an integer value for how many dice should be rolled")
print("Goodbye")
