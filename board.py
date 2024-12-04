# board.py

def create_board(): return [[" "] * 3 for _ in range(3)]

def display_board(board):
    symbols = {"X": "❌", "O": "⭕", " ": "⬜"}
    print("    0   1   2\n  +---+---+---+")
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(symbols[cell] for cell in row)} |\n  +---+---+---+")
