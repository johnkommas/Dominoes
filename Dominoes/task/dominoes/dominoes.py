# Write your code here
import random

all_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
              [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
              [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
              [3, 3], [3, 4], [3, 5], [3, 6],
              [4, 4], [4, 5], [4, 6],
              [5, 5], [5, 6],
              [6, 6]
              ]


def start_game():
    pieces = []
    for i in range(7):
        x = random.choice(all_pieces)
        all_pieces.remove(x)
        pieces.append(x)
    return pieces


def highest(pieces):
    doubles = []
    for piece in pieces:
        if piece[0] == piece[1]:
            doubles.append(piece[0])
    if doubles:
        x = max(doubles)
        return [x, x]
    else:
        return [0, 0]


while True:
    computer = start_game()
    player = start_game()
    stock = all_pieces
    computer_best_set = highest(computer)
    player_best_set = highest(player)
    if computer_best_set[0] > player_best_set[0]:
        # print('The computer makes the first move.')
        computer.remove(computer_best_set)
        status = 'player'
        snake = [computer_best_set]
        break
    elif computer_best_set[0] < player_best_set[0]:
        # print('The player makes the first move.')
        player.remove(player_best_set)
        status = 'computer'
        snake = [player_best_set]
        break
    else:
        pass


def output_results():
    print('======================================================================')
    print(f'Stock size: {len(stock)}')
    print(f'Computer pieces: {len(computer)}')
    if len(snake) <= 6:
        for i in snake:
            print(i, end="")
    else:
        for i in snake[:3]:
            print(i, end="")
        print("...", end="")
        for i in snake[-3:]:
            print(i, end="")
    print()
    print('Your pieces:')
    for a, b in enumerate(player):
        print(f"{a+1}:{b}")
    if status == 'player':
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")



def make_move():
    pass


def check_input():
    try:
        my_turn = int(input())
    except ValueError:
        print("Invalid input. Please try again.")
        return check_input()
    return my_turn


x = check_input()