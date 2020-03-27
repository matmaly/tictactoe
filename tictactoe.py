#!/usr/bin/env python3.6
def tic_tac_toe():
    user1 = "X"
    user2 = "O"
    full_board_counter = 0
    board_dict = {"1":" ",
            "2":" ",
            "3":" ",
            "4":" ",
            "5":" ",
            "6":" ",
            "7":" ",
            "8":" ",
            "9":" ",          
           }
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
    
    #Check 
    
    # Ask player 1 for input, return the result and assign it to a variable
    def player1_input():
        user1_choice = input("user1 go ")
        return user1_choice
    
    # Ask player 2 for input, return the result and assign it to a variable
    def player2_input():
        user2_choice = input("user2 go ")
        return user2_choice
    
    # Check if that field was played and return an error
    def field_played(x):
        print(x)
    
    # Loop that adds player choices to the dictionary
    draw_the_board()
    for x in board_dict:
        #field_played(x)
        user1_choice = player1_input()
        full_board_counter += 1

        # If statement that breaks the loop when the board is full 
        if full_board_counter == 9:
            board_dict[user1_choice] = user1 # Brute force, to fix later
            draw_the_board()
            break
        
        user2_choice = player2_input()
        full_board_counter += 1
        board_dict[user1_choice] = user1
        board_dict[user2_choice] = user2
        draw_the_board()

tic_tac_toe()
