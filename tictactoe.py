#!/usr/bin/env python3.6
def tic_tac_toe():
    user1 = "X"
    user2 = "O"
    move_counter = 0  
    board_not_full = True
    game_over = False
    score = {"User 1":0, "User 2":0}
    board_dict = {"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}
    
    # Function to draw the board
    def draw_the_board():
        print("     |      |     ")
        print(" ",board_dict["7"]," |  ",board_dict["8"]," | ",board_dict["9"],"  ")
        print(" ____|______|____ ")
        print("     |      |     ")
        print(" ",board_dict["4"]," |  ",board_dict["5"]," | ",board_dict["6"],"  ")
        print(" ____|______|____ ")
        print("     |      |     ")
        print(" ",board_dict["1"]," |  ",board_dict["2"]," | ",board_dict["3"],"  ")
        print("     |      |     ")
        print("-----------------")  
    
    # Ask the  player for input, return the result and assign it to a variable
    def player_input(user):
        user_choice = input(f"{user} GO! ")
        return user_choice
    
    # Check if that field was played and return an error
    def field_played(user_choice, user):
        while board_dict.get(user_choice) != " ":
            print(f"Field {board_dict.get(user_choice)} alrady played, pick another! ")
            user_choice = player_input(user)
        return user_choice
    
    # fun that checks if player has won
    def win(move_counter):
        marker = ("X","O")
        for z in marker:
            if (board_dict["1"] == board_dict["2"] == board_dict["3"] == z or
                board_dict["4"] == board_dict["5"] == board_dict["6"] == z or
                board_dict["7"] == board_dict["8"] == board_dict["9"] == z or
                board_dict["1"] == board_dict["4"] == board_dict["7"] == z or
                board_dict["2"] == board_dict["5"] == board_dict["8"] == z or
                board_dict["3"] == board_dict["6"] == board_dict["9"] == z or
                board_dict["1"] == board_dict["5"] == board_dict["9"] == z or
                board_dict["3"] == board_dict["5"] == board_dict["7"] == z):
                    print(f"{z} Won")
                    if z == "X":
                        score["User 1"] += 1
                    else:
                        score["User 2"] += 1
                    print(f"Score:\nUser 1: {score['User 1']}\nUser 2: {score['User 2']}")
                    game_over = True
                    return game_over
            elif move_counter == 9:
                print("Draw!")
                game_over = True
                return game_over


    draw_the_board()
    while board_not_full:    
        if game_over:
            new_game = input("Start a new Game? (type 'yes' or 'no' ")
            if new_game == "yes":
                board_dict = {"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}
                move_counter = 0
            else:
                break
        user1_choice = player_input("User 1")
        user1_choice = field_played(user1_choice, "User 1")
        move_counter += 1
        board_dict[user1_choice] = user1
        draw_the_board()
        game_over = win(move_counter)
        # check if var won is true, if it is, break
        if game_over:
            continue

        user2_choice = player_input("User 2")
        user2_choice = field_played(user2_choice,"User 2")
        move_counter += 1
        board_dict[user2_choice] = user2
        draw_the_board()
        game_over = win(move_counter)
        if game_over:
            continue
    else:
        print("Bye")

tic_tac_toe()
