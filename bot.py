# bot.py
import random
from logic import check_winner

# Fonction qui permet au bot de faire un mouvement
def bot_move(board, symbol, difficulty="random"):
    # Trouver toutes les cases vides sur le plateau
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    # Si aucune case vide n'est disponible, retourner None (aucun mouvement possible)
    if not empty_cells: return None

    # Identifier le symbole de l'adversaire
    opponent = "X" if symbol == "O" else "O"

    # Si la difficulté est "always-win", le bot essaie d'abord de bloquer l'adversaire, ensuite de gagner
    if difficulty == "always-win":
        # Chercher un coup pour bloquer une victoire de l'adversaire ou gagner
        for target in [opponent, symbol]:
            for r, c in empty_cells:
                board[r][c] = target  # Simuler le mouvement
                if check_winner(board) == target:
                    board[r][c] = " "  # Annuler le mouvement simulé
                    return r, c
                board[r][c] = " "  # Annuler le mouvement simulé

        # Prendre le centre si disponible
        if (1, 1) in empty_cells:
            return 1, 1

        # Chercher un coup stratégique si aucun mouvement gagnant ou bloquant n'est trouvé
        for r, c in [(0, 0), (0, 2), (2, 0), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1)]:
            if (r, c) in empty_cells:
                return r, c

    # Si aucun mouvement gagnant ou bloquant n'est trouvé, choisir aléatoirement une case vide
    return random.choice(empty_cells)