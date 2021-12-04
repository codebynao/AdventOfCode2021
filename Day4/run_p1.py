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


def get_winner(drawn_numbers, boards):
    for number in drawn_numbers.split(','):
        number = int(number)
        for board in boards:
            # line
            updated = False
            for i in range(len(board)):
                # number
                for j in range(len(board[i])):
                    if board[i][j] == number:
                        board[i][j] = ''
                        updated = True
                        break

            # No need to do the check if nothing has been updated
            if updated and is_winner(board):
                return board, number
    return None, None


def get_board_score(board, number):
    total = 0
    for line in board:
        total += sum([e for e in line if e != ''])
    return total * number


winning_board, number = get_winner(drawn_numbers, boards)

print(get_board_score(winning_board, number))
