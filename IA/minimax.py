MIN, MAX = -100000, 100000


def evaluate(board, maximize_color):
    return board.score("white") - board.score("black") if (maximize_color) == 'white' else board.score("black") - board.score("white")


def minimax(board, depth, alpha, beta, maximize_player):
    if (depth == 0 or board.game_over):
        return None, evaluate(board, maximize_player)
    moves = board.get_moves()
    best_move = moves[0]

    if maximize_player:
        max_eval = MIN
        for move in moves:
            board.make_move(move[0], move[1])
            current_eval = minimax(
                board, depth-1, alpha, beta, False)[1]
            board.unmake_move()
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = move
            alpha = max(alpha, current_eval)
            if beta <= alpha:
                break
        return best_move, max_eval
    else:
        min_eval = MAX
        for move in moves:
            board.make_move(move[0], move[1])
            current_eval = minimax(
                board, depth-1, alpha, beta, True)[1]
            board.unmake_move()
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = move
            beta = min(beta, current_eval)
            if beta <= alpha:
                break
        return best_move, min_eval
