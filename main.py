from random import seed 
from random import randint

seed(1)


def print_rules():

    print("\nWelcome to classic Tic-Tac-Toe game")
    print("You can play agains your friend or computer\n")
    print("----------RULES----------")
    print("The game is played on a grid that's 3 squares by 3 squares")
    print("First player is X, second is O")
    print("The first player to get 3 of her marks in row is the winner") 
    print("When all 9 squares are full, the game is over\n")
    print("Good luck!\n")


board = [" ", " ", " "," ", " ", " "," ", " ", " "]


def reset_stats():
    for i in range(0, 9):
        board[i] = " "


def print_board():

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "\n")


def get_board_input(user_symbol):

    user_position = -1
    is_correct = False

    while True:

        if is_correct:
            break

        user_position = input("Please enter number between 0 and 9 to fill board with new symbol: ")

        if user_position.isnumeric() == False:
            print("Enter only numbers")
            continue

        user_position = int(user_position)

        if user_position < 0 or user_position >=9:
            print("Your input is out of index")
            continue

        if board[user_position] == " ":
            is_correct = True
            board[user_position] = user_symbol


def is_winner(symbol):

    for i in range(0,3):

        if board[i] == board[i + 3] == board[i + 6] == symbol:
            return True

        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == symbol:
            return True

    if board[0] == board[4] == board[8] == user_symbol or board[2] == board[4] == board[6] == symbol:
        return True
    
    return False


def winning_position(symbol):

    for i in range(0,9):

        if board[i] == " ":
            board[i] = symbol

            if is_winner(symbol):
                board[i] = " "
                return i

            board[i] = " "

    return -1

def computer_play(counter):

    if counter >= 2:

        b = winning_position("O")

        if b == -1:
            c = winning_position("X")

            if c == -1:
                for i in range(0,9):

                    if board[i] == " ":
                        board[i] = "O"
                        return
            else:
                board[c] = "O"

        else:
            board[b] = "O"

    else: 

        if board[4] == " ":
            board[4] = "O"

        else:

            a = randint(0,4)

            if a == 1:
                board[0] = "O"

            elif a == 2:
                board[2] = "O"

            elif a == 3:
                board[6] = "O"

            else:
                board[8] = "O" 


def play_against(second_player):

    counter = 0

    while True:

        if counter == 9:
            return -1

        if counter % 2 == 0:
            get_board_input("X")

            print_board()

            if counter >= 4:
                if is_winner("X"):
                    return 0
        else:

            if second_player == "friend":
                get_board_input("O")
            else:
                computer_play(counter)
                print("Computer Play")   

            print_board()

            if counter >= 4:
                if is_winner("O"):
                    return 1
        counter += 1


def start_game():

    reset_stats()

    player_one = input("Enter first players name: ")
    player_two = input("Enters second players name, write -computer- if you want to play against PC: ")

    player_one = player_one.lower()
    player_two = player_two.lower()

    winner = 0
    counter = 0

    print("Let's Gooooooooooooooooooooooooooooooooooooooooooooooooooooo!\n")

    print_board()

    if player_two == "computer":

        winner = play_against("computer")

    else:

        winner = play_against("friend")

    if winner == 1:
        
        if player_two == "computer":
            print("User you lost that game :(")

        else: 
            print("Congrats " + player_two + " you win :)")

    elif winner == 0: 
        print("Congrats " + player_one + " you win :)")

    else:

        print("There is a draw")

#----------------------------RUN----------------------------
print_rules()

play_game = ""

while True:

    play_game = input("\nIf you want to exit from game, write -exit-, write anything to continue: ")
    print("\n")
    play_game = play_game.lower()

    if play_game == "exit":
        break

    start_game()