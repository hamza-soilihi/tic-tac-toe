from board import create_board, display_board
from logic import add_symbol, check_winner
from player import get_player_symbol, get_player_move
from bot import bot_move

def play_game():
    while True:
        # Créer le plateau de jeu et initialiser les joueurs
        board, p1, p2 = create_board(), *get_player_symbol()
        print(f"🎮 Joueur 1: {p1}, Joueur 2: {p2}")
        display_board(board)

        # Définir le type de chaque joueur (humain ou bot)
        p_types = {1: "h", 2: ""}
        while p_types[2] not in ("h", "r", "w"):
            p_types[2] = input("👤 Joueur 2: humain (h) ou bot (r/w) ? ").lower()
            if p_types[2] not in ("h", "r", "w"):
                print("Choix invalide. Veuillez entrer 'h' pour humain, 'r' pour bot (random), ou 'w' pour bot (always-win).")

        current, symbols, result = 1, [p1, p2], "➡️ Joueur suivant"

        # Boucle principale du jeu
        while result == "➡️ Joueur suivant":
            # Obtenir le mouvement (humain ou bot)
            move = get_player_move() if p_types[current] == "h" else bot_move(board, symbols[current - 1], "always-win" if p_types[current] == "w" else "random")
            if move is None:
                break

            # Ajouter le symbole et vérifier le résultat
            if add_symbol(board, *move, symbols[current - 1]):
                display_board(board)
                result = check_winner(board)
                print(result)
                current = 1 if current == 2 else 2

        # Demander si le joueur souhaite rejouer
        replay = ""
        while replay not in ('oui', 'o', 'yes', 'y', 'non', 'n', 'no'):
            replay = input("🔄 Rejouer ? (oui/non): ").lower()
            if replay not in ('oui', 'o', 'yes', 'y', 'non', 'n', 'no'):
                print("Choix invalide. Veuillez entrer 'oui' (o) ou 'non' (n).")
        if replay not in ('oui', 'o', 'yes', 'y'):
            break

# Lancer le jeu
if __name__ == "__main__":
    play_game()
