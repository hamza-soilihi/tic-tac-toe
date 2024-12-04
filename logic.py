# logic.py

def add_symbol(board, row, col, symbol):
    if board[row][col] == " ": board[row][col] = symbol; return True
    print("⚠️ Case occupée"); return False

def check_winner(board):
   # Cette ligne crée une liste appelée 'lines' qui combine toutes les lignes, colonnes et diagonales du plateau de jeu 'board'.
   # Elle est composée de trois parties : 
   # 1 'board' : Ajoute toutes les lignes du plateau à la liste 'lines'.
   # 2 [[board[r][c] for r in range(3)] for c in range(3)]' : Utilise une liste par compréhension pour ajouter toutes les colonnes du plateau à 'lines'.
   # 3 [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]' : Ajoute les deux diagonales du plateau à 'lines'.
   # En résumé, 'lines' contient toute les conbinaison possible pour une victoire.
    lines = board + [[board[r][c] for r in range(3)] for c in range(3)] + [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    for line in lines:
        #cette ligne de code permet de vérifier s'il y a une rangée complète # de trois symboles identiques ('X' ou 'O') dans le jeu, ce qui indiquerait une victoire.
        if line[0] == line[1] == line[2] and line[0] in ["X", "O"]:
            return f"🏆 Victoire: {line[0]}"
    return "🤝 Match nul" if all(cell != " " for row in board for cell in row) else "➡️ Joueur suivante"
