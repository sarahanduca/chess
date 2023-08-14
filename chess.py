import chess
import minimax
import math
import random
import sys

MIN, MAX = -100000, 100000


def main():
    board = chess.Board()
    turn = "White"
    player = []
    ai = []
    while not board.is_game_over():
        legal_moves = True
        print('--------------------------------------------')
        print(board)
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
            move, score = minimax.minimax(board, 4, MIN, MAX, True)
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