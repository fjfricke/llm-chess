import chess
import random
import lmql
import asyncio

def does_ai_start():
    return random.randint(0, 1) == 0


async def play():
    with open('src/chess.lmql', 'r') as f:
        query = f.read()
    board = chess.Board()
    next_move_is_ai = does_ai_start()
    color_ai = "white" if next_move_is_ai else "black"
    color_human = "black" if next_move_is_ai else "white"
    while not board.is_game_over():
        print("You are playing as " + color_human + ".")
        while True:
            print(board)
            if next_move_is_ai:
                answer = await lmql.run(
                    query,
                    color=color_ai,
                    fen=board.board_fen(),
                    legal_moves=set([board.san(uci) for uci in board.legal_moves]),
                    model="openai/gpt-3.5-turbo-instruct")
                print("AI reasoning: " + answer.variables["REASONING"])
                move = answer.variables["MOVE"]
            else:
                move = input("Move: ")
            try:
                board.push_san(move)
            except chess.InvalidMoveError:
                print("Invalid move")
                continue
            except chess.IllegalMoveError:
                print("Illegal move")
                continue
            except chess.AmbiguousMoveError:
                print("Ambiguous move")
                continue
            # print(board.board_fen())
            next_move_is_ai = not next_move_is_ai
            


def main():
    asyncio.run(play())


if __name__ == "__main__":
    main()