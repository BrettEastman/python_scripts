gameboard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board(gameboard):
    print("Here is the current gameboard: ")
    print(gameboard[1] + '|' + gameboard[2] + '|' + gameboard[3])
    print('-----')
    print(gameboard[4] + '|' + gameboard[5] + '|' + gameboard[6])
    print('-----')
    print(gameboard[7] + '|' + gameboard[8] + '|' + gameboard[9])


def player_input():
    marker = ""

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def position_choice():
    choice = 'notadigit'
    acceptable_range = range(1, 10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input('Please choose a position number (1-9): ')
        if choice.isdigit() == False:
            print("Sorry, this is not a digit.")
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, this is not in an acceptable range.")
                within_range = False

    return int(choice)


def replacement_choice1(gameboard, position):
    user_placement1 = player1_marker

    gameboard[position] = user_placement1

    return gameboard


def replacement_choice2(gameboard, position):
    user_placement2 = player2_marker

    gameboard[position] = user_placement2

    return gameboard


def find_three_x():
    resx = [i for i, e in enumerate(gameboard) if e == 'X']
    if resx == [1, 2, 3]:
        return True
    elif resx == [4, 5, 6]:
        return True
    elif resx == [7, 8, 9]:
        return True
    elif resx == [1, 5, 9]:
        return True
    elif resx == [3, 5, 7]:
        return True
    elif resx == [1, 4, 7]:
        return True
    elif resx == [2, 5, 8]:
        return True
    elif resx == [3, 6, 9]:
        return True
    else:
        return False


def find_three_o():
    reso = [i for i, e in enumerate(gameboard) if e == 'O']
    if reso == [1, 2, 3]:
        return True
    elif reso == [4, 5, 6]:
        return True
    elif reso == [7, 8, 9]:
        return True
    elif reso == [1, 5, 9]:
        return True
    elif reso == [3, 5, 7]:
        return True
    elif reso == [1, 4, 7]:
        return True
    elif reso == [2, 5, 8]:
        return True
    elif reso == [3, 6, 9]:
        return True
    else:
        return False


def gameon_choice():
    choice = 'notYorN'

    while choice not in ['Y', 'N']:
        choice = input('Would you like to continue? (Y or N):')
        if choice not in ['Y', 'N']:
            print('Please choose Y or N.')

    if choice == 'Y':
        return True
    else:
        return False


result = input("Would you like to play 'Tic Tac Toe?'(Y or N): ")

if result == 'Y':
    display_board(gameboard)
    game_on = True
else:
    game_on = False

player1_marker, player2_marker = player_input()

while game_on == True:

    # player1
    position = position_choice()

    replacement_choice1(gameboard, position)

    display_board(gameboard)

    # if three, break from the while loop and print you win
    announce1 = find_three_x()
    if announce1:
        print("The X's win!")
        break

    announce2 = find_three_o()
    if announce2:
        print("The O's win!")
        break

    # player2
    position = position_choice()

    replacement_choice2(gameboard, position)

    display_board(gameboard)

    # if three, break from the while loop and print you win
    announce1 = find_three_x()
    if announce1:
        print("The X's win!")
        break

    announce2 = find_three_o()
    if announce2:
        print("The O's win!")
        game_on = gameon_choice()
        break


print("Game over. Thanks for playing!")