# bot.py
import random
from logic import check_winner

# Fonction qui permet au bot de faire un mouvement
# Paramètres :
# - board : l'état actuel du plateau de jeu (une matrice 3x3)
# - symbol : le symbole du bot ("X" ou "O")
# - difficulty : niveau de difficulté du bot (par défaut "random", sinon "always-win")
def bot_move(board, symbol, difficulty="random"):
    # Trouver toutes les cases vides sur le plateau
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    # Si aucune case vide n'est disponible, retourner None (aucun mouvement possible)
    if not empty_cells: return None

    # Identifier le symbole de l'adversaire (si le bot est "O", l'adversaire est "X" et vice versa)
    opponent = "X" if symbol == "O" else "O"

    # Si la difficulté est "always-win", le bot essaie de gagner ou de bloquer l'adversaire
    if difficulty == "always-win":
        # Chercher un coup gagnant pour le bot
        for r, c in empty_cells:
            board[r][c] = symbol  # Simuler le mouvement
            # Si ce mouvement fait gagner le bot, retourner cette position
            if check_winner(board).startswith("\ud83c\udf40"): 
                board[r][c] = " "  # Annuler le mouvement simulé
                return r, c
            board[r][c] = " "  # Annuler le mouvement simulé

        # Chercher un coup pour bloquer une victoire de l'adversaire
        for r, c in empty_cells:
            board[r][c] = opponent  # Simuler le mouvement de l'adversaire
            # Si l'adversaire gagne avec ce mouvement, retourner cette position pour bloquer
            if check_winner(board).startswith("\ud83c\udf40"): 
                board[r][c] = " "  # Annuler le mouvement simulé
                return r, c
            board[r][c] = " "  # Annuler le mouvement simulé

    # Si aucun mouvement gagnant ou bloquant n'est trouvé, choisir aléatoirement une case vide
    return random.choice(empty_cells)