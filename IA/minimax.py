MIN, MAX = -100000, 100000


def evaluate(board, maximize_color):
    return board.score("white") - board.score("black") if (maximize_color) == 'white' else board.score("black") - board.score("white")


def minimax(board, depth, alpha, beta, maximize_player):
    if (depth == 0 or board.game_over):
        return None, evaluate(board, "white" if maximize_player else "black")
    # moves = [item for sub_list in board.get_valid_moves() for item in sub_list]
    moves = board.get_valid_moves()
    best_move = [moves[0][0], moves[1][0]]

    if maximize_player:
        max_eval = MIN
        for pieces in moves:
            for cord in pieces[1]:
                prev_position = pieces[0].pos
                print(prev_position)
                board.make_move(pieces[0], cord)
                curr_eval = minimax(
                    board, depth-1, alpha, beta, False)[1]
                board.unmake_move(pieces[0], prev_position)
                if curr_eval > max_eval:
                    max_eval = curr_eval
                    best_move = [pieces[0], cord]
                alpha = max(alpha, curr_eval)
                if beta <= alpha:
                    break
        return best_move, max_eval
    else:
        min_eval = MAX
        for pieces in moves:
            for cord in pieces[1]:
                board.make_move(pieces[0], cord)
                curr_eval = minimax(
                    board, depth-1, alpha, beta, True)[1]
                board.unmake_move(pieces[0], prev_position)
                if curr_eval < min_eval:
                    min_eval = curr_eval
                    best_move = [pieces[0], cord]
                beta = min(beta, curr_eval)
                if beta <= alpha:
                    break
        return best_move, min_eval
