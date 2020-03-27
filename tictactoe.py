#!/usr/bin/env python3.6
def tic_tac_toe():
    user1 = "X"
    user2 = "O"
    full_board_counter = 0
    board_not_full = True
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
    def win():
        if (board_dict["1"] == board_dict["2"] == board_dict["3"] or
            board_dict["4"] == board_dict["5"] == board_dict["6"] or
            board_dict["7"] == board_dict["8"] == board_dict["9"] or
            board_dict["1"] == board_dict["4"] == board_dict["7"] or
            board_dict["2"] == board_dict["5"] == board_dict["8"] or
            board_dict["3"] == board_dict["6"] == board_dict["9"] or
            board_dict["1"] == board_dict["5"] == board_dict["9"] or
            board_dict["3"] == board_dict["5"] == board_dict["7"]):
            print(f"{board_dict['1']} Won")
            return break
        
    draw_the_board()
    while board_not_full:    
        user1_choice = player_input("User 1")
        user1_choice = field_played(user1_choice, "User 1")
        full_board_counter += 1
        board_dict[user1_choice] = user1
        draw_the_board()
        win()
        # If statement that breaks the loop when the board is full 
        if full_board_counter == 9:
            board_dict[user1_choice] = user1 # Brute force, to fix later
            draw_the_board()
            break
        
        user2_choice = player_input("User 2")
        user2_choice = field_played(user2_choice,"User 2")
        full_board_counter += 1
        board_dict[user2_choice] = user2
        draw_the_board()
        win()
    else:
        print("Start a new game?")

tic_tac_toe()
