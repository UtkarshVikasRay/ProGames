import random

PLAYER = "X"
AI = "O"

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def is_draw(board):
    return all(cell in [PLAYER, AI] for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] not in [PLAYER, AI]]

def minimax(board, is_maximizing):
    if is_winner(board, AI):
        return 1
    elif is_winner(board, PLAYER):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for (i, j) in get_available_moves(board):
            board[i][j] = AI
            score = minimax(board, False)
            board[i][j] = str(3 * i + j + 1)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for (i, j) in get_available_moves(board):
            board[i][j] = PLAYER
            score = minimax(board, True)
            board[i][j] = str(3 * i + j + 1)
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = AI
        score = minimax(board, False)
        board[i][j] = str(3 * i + j + 1)
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def main():
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    print("Welcome to Tic Tac Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Player move
        move = int(input("Enter your move (1-9): ")) - 1
        i, j = divmod(move, 3)
        if board[i][j] in [PLAYER, AI]:
            print("Invalid move. Try again.")
            continue
        board[i][j] = PLAYER
        print_board(board)

        if is_winner(board, PLAYER):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        i, j = best_move(board)
        board[i][j] = AI
        print("AI move:")
        print_board(board)

        if is_winner(board, AI):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
