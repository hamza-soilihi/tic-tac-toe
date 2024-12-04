# main.py

from board import create_board, display_board
from logic import add_symbol, check_winner
from player import get_player_symbol, get_player_move
from bot import bot_move

def play_game():
    while True:
        board, p1, p2 = create_board(), *get_player_symbol()
        print(f"🎮 Joueur 1: {p1}, Joueur 2: {p2}"); display_board(board)
        p_types = {1: "h", 2: input("👤 Joueur 2: humain (h) ou bot (r/w) ? ").lower()}
        current, symbols = 1, [p1, p2]

        while (result := "➡️ Joueur suivant") == "➡️ Joueur suivant":
            move = get_player_move() if p_types[current] == "h" else bot_move(board, symbols[current - 1], "always-win" if p_types[current] == "w" else "random")
            if move is None: break
            elif add_symbol(board, *move, symbols[current - 1]):
                display_board(board); result = check_winner(board); print(result)
                current = 1 if current == 2 else 2

        if input("🔄 Rejouer ? (oui/non): ").lower() != 'oui': break

if __name__ == "__main__": play_game()