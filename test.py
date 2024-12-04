
while (result := "➡️ Joueur suivant") == "➡️ Joueur suivant":
    move = get_player_move() if p_types[current] == "h" else bot_move(board, symbols[current - 1], "always-win" if p_types[current] == "w" else "random")