MIN, MAX = -100000, 100000


def evaluate(board, max_color):
    return board.whiteScore - board.blackScore if (max_color) == 'white' else board.blackScore - board.whiteScore


def minimax(board, depth, alpha, beta, maximize_agent, max_color):
    if (depth == 0 or board.game_over):
        return None, evaluate(board, max_color)
    moves = board.get_moves()
    best_move = random.choice(moves)

    if maximize_agent:
        max_eval = MIN
        for move in moves:
            board.make_move(move[0], move[1])
            current_eval = minimax(
                board, depth-1, alpha, beta, False, max_color)[1]
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
                board, depth-1, alpha, beta, True, max_color)[1]
            board.unmake_move()
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = move
            beta = min(beta, current_eval)
            if beta <= alpha:
                break
        return best_move, min_eval
