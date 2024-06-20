# Initialize the Tic-Tac-Toe board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]


# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


# Check for available moves
def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']


# Check for a win
def check_win(board, player):
    win_states = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for state in win_states:
        if all([board[x][y] == player for x, y in state]):
            return True
    return False


# Check for a draw
def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])


# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 10 - depth
    if check_win(board, 'X'):
        return depth - 10
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# Find the best move
def find_best_move(board):
    best_val = -float('inf')
    best_move = None
    for move in available_moves(board):
        board[move[0]][move[1]] = 'O'
        move_val = minimax(board, 0, False, -float('inf'), float('inf'))
        board[move[0]][move[1]] = ' '
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move


def play_game():
    board = initialize_board()
    current_player = 'X'  # Human starts first

    while True:
        print_board(board)
        if current_player == 'X':
            try:
                row, col = map(int, input("Enter your move (row and column): ").split())
            except ValueError:
                print("Invalid input. Please enter row and column as two numbers separated by a space.")
                continue

            if row not in range(3) or col not in range(3):
                print("Invalid move. Please enter row and column values between 0 and 2.")
                continue

            if board[row][col] != ' ':
                print("Invalid move. The cell is already occupied. Try again.")
                continue
        else:
            move = find_best_move(board)
            row, col = move

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


# Start the game
play_game()
