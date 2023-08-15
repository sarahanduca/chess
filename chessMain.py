import chess
import chess.svg
import IA.minimax as minimax
import math
import random
import sys

MIN, MAX = -100000, 100000


def display_text_board(board):
    # Create a mapping for file and rank names
    file_names = ' abcdefgh'
    rank_names = ' 12345678'

    # Print the column headers (files)
    # print('   ' + '  '.join(file_names[1:9]))

    # Loop through ranks in reverse order
    for rank in range(7, -1, -1):
        row = []
        # Loop through files
        for file in range(8):
            square = chess.square(file, rank)
            piece = board.piece_at(square)
            if piece:
                row.append(piece.symbol())
            else:
                row.append(' ')
        # Print rank name and row
        print(rank_names[rank + 1] + ' | ' + ' | '.join(row) + ' | ')
        print('  ---------------------------------')

    # Print the column headers (files) again at the bottom
    print('    ' + '   '.join(file_names[1:9]))


def main():
    board = chess.Board()
    turn = "White"
    player = []
    ai = []
    count = 0

    while not board.is_game_over():
        legal_moves = True
        print('Jogada', count)
        count += 1
        # You can set any desired position here
        display_text_board(board)
        # print(board)
        if turn == "White":
            print("Movimentos Permitidos: ", board.legal_moves)
            while legal_moves:
                move = input("Escreva seu movimento: ")
                if chess.Move.from_uci(move) in board.legal_moves:
                    move = chess.Move.from_uci(str(move))
                    legal_moves = False
                else:
                    print("Movimento inválido")
            player.append(move)
            board.push(move)
            turn = "Black"
        else:
            move, score = minimax.minimax(board, 4, MIN, MAX, True, 'B')
            print(move, score)
            board.push(move)
            turn = "White"
            ai.append(move)
    outcome = board.outcome()
    if outcome.winner == chess.WHITE:
        print("White wins!")
        outcomeText = "White wins!"
    elif outcome.winner == chess.BLACK:
        print("Black wins!")
        outcomeText = "Black wins!"
    else:
        print("Draw!")
        outcomeText = "Draw!"
    writeOnFile(player, ai, outcomeText)


def writeOnFile(player, ia, outcomeText):
    file = open("Jogadas.txt", "w")
    file.write("Player: ")
    for i in player:
        file.write(str(i) + " ")
    file.write("\n")
    file.write("IA: ")
    for i in ia:
        file.write(str(i) + " ")
    file.write("\n")
    file.write("Resultado: " + outcomeText)
    file.close()


if __name__ == "__main__":
    main()
