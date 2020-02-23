print("there are 12 coins you go first and take 1 2 or 3 coins, you win by taking the last coin")
rounds_completed = 0
while rounds_completed == 0:
    player_move_defined = 0
    while player_move_defined == 0:
        try:
            first_player_move = int(input("how many coins will you take"))
            player_move_defined = 1
        except:
            print("You must enter an integer value")
    if 0 < first_player_move < 4:
        first_computer_move = 4 - first_player_move
        print("The computer will take", first_computer_move, "coin(s), there are now 8 coins remaining")
        rounds_completed = rounds_completed + 1
    else:
        print("You must choose a number between 1 and 3")
while rounds_completed == 1:
    player_move_defined = 0
    while player_move_defined == 0:
        try:
            second_player_move = int(input("how many coins will you take"))
            player_move_defined = 1
        except:
            print("You must enter an integer value")
    if 0 < second_player_move < 4:
        second_computer_move = 4 - second_player_move
        print("The computer will take", second_computer_move, "coin(s), there are now 4 coins remaining")
        rounds_completed = rounds_completed + 1
    else:
        print("You must choose a number between 1 and 3")
while rounds_completed == 2:
    player_move_defined = 0
    while player_move_defined == 0:
        try:
            third_player_move = int(input("how many coins will you take"))
            player_move_defined = 1
        except:
            print("You must enter an integer value")
    if 0 < third_player_move < 4:
        third_computer_move = 4 - third_player_move
        print("The computer will take", third_computer_move, "coin(s), the computer wins")
        rounds_completed = rounds_completed + 1
    else:
        print("You must choose a number between 1 and 3")