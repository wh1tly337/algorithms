def play_game(s1, s2):
    num_moves = 0
    while s1 + s2 < 77:
        if s1 <= s2:
            s1 *= 2
        else:
            s2 *= 2
        num_moves += 1
    return num_moves


max_moves = 0
max_moves_start_positions = []
for s1 in range(1, 70):
    for s2 in range(1, 70):
        num_moves = play_game(s1, s2)
        if num_moves > max_moves:
            max_moves = num_moves
            max_moves_start_positions = [(s1, s2)]
        elif num_moves == max_moves:
            max_moves_start_positions.append((s1, s2))

# Выводим результат
print("Максимальное количество ходов:", max_moves)
print("Начальные позиции с максимальным количеством ходов:")
for pos in max_moves_start_positions:
    print(pos)
