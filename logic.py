# logic.py

def add_symbol(board, row, col, symbol):
    if board[row][col] == " ": board[row][col] = symbol; return True
    print("⚠️ Case occupée"); return False

def check_winner(board):
    #liste par comprehenhension
    #board[r][c] : Cette partie accède à l'élément du plateau (board) à la ligne r et à la colonne c
    #for r in range(3) : cela signifie que r va prendre successivement les valeurs 0, 1 et 2. La boucle itère donc sur les trois premières lignes du plateau.
    lines = board + [[board[r][c] for r in range(3)] for c in range(3)] + [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] in ["X", "O"]:
            return f"🏆 Victoire: {line[0]}"
    return "🤝 Match nul" if all(cell != " " for row in board for cell in row) else "➡️ Joueur suivant"
