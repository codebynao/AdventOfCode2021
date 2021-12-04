with open('./input.txt', 'r') as textInput:
    data = textInput.readlines()

drawn_numbers = data.pop(0)

boards = []
for index in range(0, len(data), 6):
    board = []
    # Skip i = 0 because it is an empty line
    for i in range(1, 6):
        board_line = data[index + i]
        board.append([int(number) for number in board_line.split(' ') if len(number.strip()) > 0])
    boards.append(board)


def is_winner(board):
    for i in range(len(board)):
        if all(j == '' for j in board[i]) or all(board[j][i] == '' for j in range(len(board))):
            return True
    return False


def get_winners(drawn_numbers, boards):
    winners = {}
    for number in drawn_numbers.split(','):
        number = int(number)
        for idx, board in enumerate(boards):
            # Check if the board is already in the winning boards
            if idx in winners:
                continue

            updated = False
            # line
            for i in range(len(board)):
                # number
                for j in range(len(board[i])):
                    if board[i][j] == number:
                        board[i][j] = ''
                        updated = True
                        break

            # No need to do the check if nothing has been updated
            if updated and is_winner(board):
                winners[idx] = (board, number)
    return winners


def get_board_score(board, number):
    total = 0
    for line in board:
        total += sum([e for e in line if e != ''])
    return total * number


winners = get_winners(drawn_numbers, boards)
winner_idx = list(winners.keys())[-1] if len(list(winners.keys())) > 0 else None

if winner_idx:
    print(get_board_score(winners[winner_idx][0], winners[winner_idx][1]))
else:
    print('No winner...')
