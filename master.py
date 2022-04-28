# Edited
# Github: https://github.com/navdeeshahuja/Python-TicTacToe-Best-Move-Generator-Artificial-Intelligence-Minimax

def check_win(board, player):
    for i in range(0, 7, 3):
        if board[i] == player and board[i + 1] == player and board[i + 2] == player:
            return True
    for i in range(0, 3):
        if board[i] == player and board[i + 3] == player and board[i + 6] == player:
            return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False


def check_lose(board, player):
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    if check_win(board, opponent):
        return True
    return False


def check_tie(board):
    for x in board:
        if x == " ":
            return False
    return True


def get_ai_move(board, next_move, ai_player):
    if check_win(board, ai_player):
        return -1, 10
    elif check_lose(board, ai_player):
        return -1, -10
    elif check_tie(board):
        return -1, 0

    moves = []

    for i in range(len(board)):
        if board[i] == " ":
            board[i] = next_move

            score = get_ai_move(board, ("X" if next_move == "O" else "O"), ai_player)[1]
            moves.append((i, score))
            board[i] = " "

    if next_move == ai_player:
        max_score = moves[0][1]
        best_move = moves[0]
        for move in moves:
            if move[1] > max_score:
                best_move = move
                max_score = move[1]
        return best_move
    else:
        min_score = moves[0][1]
        worst_move = moves[0]
        for move in moves:
            if move[1] < min_score:
                worst_move = move
                min_score = move[1]
        return worst_move
