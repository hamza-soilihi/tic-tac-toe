# player.py

def get_player_symbol():
    # Boucle 'while' utilisant l'opérateur d'affectation := (walrus operator). # Cette boucle continue de demander à l'utilisateur de choisir un symbole (❌/⭕)
    # et convertit l'entrée en majuscule avec .upper() Tant que l'entrée n'est pas "X" ou "O", la boucle continue de demander un symbole valide.
    while (symbol := input("🎮 Choisissez un symbole (❌/⭕): ").upper()) not in ["X", "O"]:
        print("⚠️ Symbole invalide, choisissez ❌ ou ⭕.")
    return symbol, "O" if symbol == "X" else "X"

def get_player_move():
    while True:
        try:
            # Essaie de lire deux entiers de l'utilisateur : 'row' pour la ligne et 'col' pour la colonne
            # Convertit les entrées en entiers en utilisant int()
            row, col = int(input("📝 Ligne (0-2): ")), int(input("📝 Colonne (0-2): "))
            # Vérifie si les valeurs de 'row' et 'col' sont dans l'intervalle de 0 à 2 (inclus)
            # Si oui, retourne les valeurs de 'row' et 'col', ce qui termine la boucle 'while'
            if row in range(3) and col in range(3): return row, col
        # Si une erreur de valeur se produit (par exemple, si l'entrée n'est pas un entier),
        # ignore l'erreur et continue la boucle essaie
        except ValueError: pass
        print("⚠️ Valeurs entre 0 et 2.")
