# player.py

def get_player_symbol():
    while (symbol := input("🎮 Choisissez un symbole (❌/⭕): ").upper()) not in ["X", "O"]:
        print("⚠️ Symbole invalide, choisissez ❌ ou ⭕.")
    return symbol, "O" if symbol == "X" else "X"

def get_player_move():
    while True:
        try:
            row, col = int(input("📝 Ligne (0-2): ")), int(input("📝 Colonne (0-2): "))
            if row in range(3) and col in range(3): return row, col
        except ValueError: pass
        print("⚠️ Valeurs entre 0 et 2.")
