import math
import chess

def get_piece_value(piece, maximize_color):
    if piece.piece_type == 1:
        return 10 if piece.color == maximize_color else -10
    elif piece.piece_type == 2:
        return 30 if piece.color == maximize_color else -30
    elif piece.piece_type == 3:
        return 30 if piece.color == maximize_color else -30
    elif piece.piece_type == 4:
        return 50 if piece.color == maximize_color else -50
    elif piece.piece_type == 5:
        return 90 if piece.color == maximize_color else -90
    elif piece.piece_type == 6:
        return 900 if piece.color == maximize_color else -900
    else:
        return 0

def evaluate(board, maximize_color):
    value = 0
    for i in range(64):
        piece = board.piece_at(i)
        if piece is not None:
            value += abs(get_piece_value(piece, maximize_color))
    return value if maximize_color else value * -1
    

def minimax(board, depth, alpha, beta, maximize_player):
    if (depth == 0 or board.is_game_over()):
        return None, evaluate(board, maximize_player)
    best_move = None
    if maximize_player:
        best_value = -math.inf
        for move in board.legal_moves:
            mv = chess.Move.from_uci(str(move))
            board.push(mv)
            value = minimax(board, depth - 1, alpha, beta, False)[1]
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
            value = minimax(board, depth - 1, alpha, beta, True)[1]
            board.pop()
            if value < best_value:
                best_value = value
                best_move = mv
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_move, best_value