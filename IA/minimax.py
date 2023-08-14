import math
import chess


def get_piece_value(piece, maximize_color):
    # precisa retornar o valor dependendo da cor
    piece_color = piece.color if maximize_color == 'W' else not piece.color
    if piece.piece_type == 1:
        return 10 if piece_color == maximize_color else -10
    elif piece.piece_type == 2:
        return 30 if piece_color == maximize_color else -30
    elif piece.piece_type == 3:
        return 30 if piece_color == maximize_color else -30
    elif piece.piece_type == 4:
        return 50 if piece_color == maximize_color else -50
    elif piece.piece_type == 5:
        return 90 if piece_color == maximize_color else -90
    elif piece.piece_type == 6:
        return 900 if piece_color == maximize_color else -900
    else:
        return 0


def evaluate(board, maximize_color):
    value = 0
    for i in range(64):
        piece = board.piece_at(i)
        if piece is not None:
            value += get_piece_value(piece, maximize_color)
    return value


def minimax(board, depth, alpha, beta, maximize_player, maximize_color):
    if (depth == 0 or board.is_game_over()):
        return None, evaluate(board, maximize_color)
    best_move = None
    if maximize_player:
        best_value = -math.inf
        for move in board.legal_moves:
            mv = chess.Move.from_uci(str(move))
            board.push(mv)
            value = minimax(board, depth - 1, alpha, beta,
                            False, maximize_color)[1]
            board.pop()
            if value > best_value:
                best_value = value
                best_move = mv
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_move, best_value
    else:
        best_value = math.inf
        for move in board.legal_moves:
            mv = chess.Move.from_uci(str(move))
            board.push(mv)
            value = minimax(board, depth - 1, alpha,
                            beta, True, maximize_color)[1]
            board.pop()
            if value < best_value:
                best_value = value
                best_move = mv
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_move, best_value
