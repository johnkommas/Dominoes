# Write your code here
import random
import sys

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


def output_results():
    print('======================================================================')
    print(f'Stock size: {len(stock)}')
    print(f'Computer pieces: {len(computer)}')
    print()
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
    print()
    print('Your pieces:')
    for a, b in enumerate(player):
        print(f"{a + 1}:{b}")
    if status == 'player' and len(computer) > 0:
        print("Status: It's your turn to make a move. Enter your command.")
    elif status == 'player' and len(computer) == 0:
        print("Status: The game is over. The computer won!")
        return True
    elif status == 'computer' and len(player) > 0:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        response = input()
    elif status == 'computer' and len(player) == 0:
        print("Status: The game is over. You won!")
        return True


def make_move(turn_player):
    if status == 'player':
        try:
            decision = int(input())
            if abs(decision) > len(player):
                print("Invalid input. Please try again.")
                return make_move(turn_player)
        except ValueError:
            print("Invalid input. Please try again.")
            return make_move(turn_player)

    elif status == 'computer':
        count = count_numbers()
        computer_pieces = get_scores(count)
        decision = pick_side(computer_pieces)

    val = turn_player[abs(decision) - 1]
    # Select a domino and place it on the left side of the snake.
    if decision < 0:
        if snake[0][0] == val[1]:
            snake.insert(0, val)
            turn_player.remove(val)
        elif snake[0][0] == val[0]:
            val.reverse()
            snake.insert(0, val)
            val.reverse()
            turn_player.remove(val)
        else:
            if status == 'computer':
                return make_move(turn_player)
            elif status == 'player':
                print("Illegal move. Please try again.")
                return make_move(turn_player)

    # Select a domino and place it on the right side of the snake.
    elif decision > 0:
        if snake[-1][-1] == val[0]:
            snake.append(val)
            turn_player.remove(val)
        elif snake[-1][-1] == val[1]:
            val.reverse()
            snake.insert(0, val)
            val.reverse()
            turn_player.remove(val)
        else:
            if status == 'computer':
                return make_move(turn_player)
            elif status == 'player':
                print("Illegal move. Please try again.")
                return make_move(turn_player)

    # Take an extra piece from the stock (if it's not empty) and skip a turn.
    else:
        if stock:
            turn_player.append(stock.pop())
        else:
            print("Status: The game is over. It's a draw!")
            sys.exit(1)


def count_numbers():
    count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for num_set in snake:
        first = num_set[0]
        second = num_set[1]
        count[first] += 1
        count[second] += 1
    for piece in computer:
        first = piece[0]
        second = piece[1]
        count[first] += 1
        count[second] += 1
    return count


def pick_side(computer_pieces):
    for computer_piece in computer_pieces:
        if snake[0][0] in computer_piece[-1]:
            return -1 * (computer.index(computer_piece[-1]) + 1)
        elif snake[-1][-1] in computer_piece[-1]:
            return +1 * (computer.index(computer_piece[-1]) + 1)
    return 0


def get_scores(count):
    score = []
    for piece in computer:
        score.append(count[piece[0]] + count[piece[1]])
    sorted_pieces = list(zip(score, computer))
    sorted_pieces.sort()
    return sorted_pieces


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

while True:
    end_game = output_results()
    if end_game:
        break
    if status == 'player':
        make_move(player)
        status = 'computer'
    elif status == 'computer':
        make_move(computer)
        status = 'player'
