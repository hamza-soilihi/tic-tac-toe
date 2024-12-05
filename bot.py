# bot.py
import random
from logic import check_winner

def bot_move(board, symbol, difficulty="random"):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if not empty_cells: return None
    opponent = "X" if symbol == "O" else "O"
    if difficulty == "always-win":
        for r, c in empty_cells:
            board[r][c] = symbol
            if check_winner(board).startswith("🏆"): board[r][c] = " "; return r, c
            board[r][c] = " "
        for r, c in empty_cells:
            board[r][c] = opponent
            if check_winner(board).startswith("🏆"): board[r][c] = " "; return r, c
            board[r][c] = " "
    return random.choice(empty_cells)