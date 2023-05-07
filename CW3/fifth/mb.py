from functools import lru_cache


@lru_cache(None)
def game(s1, s2):
    # Если одна из куч содержит уже 77 камней или более, то игра заканчивается
    if s1 >= 77 or s2 >= 77:
        return 0

    # Ход Пети
    petia_options = []
    if s1 < 77:
        petia_options.append(1 + game(s1 + 1, s2))
        petia_options.append(1 + game(s1 * 2, s2))
    if s2 < 77:
        petia_options.append(1 + game(s1, s2 + 1))
        petia_options.append(1 + game(s1, s2 * 2))
    petia_moves = min(petia_options) if petia_options else float('inf')

    # Ход Вани
    vania_options = []
    if s1 < 77:
        vania_options.append(1 + game(s1 + 1, s2))
        vania_options.append(1 + game(s1 * 2, s2))
    if s2 < 77:
        vania_options.append(1 + game(s1, s2 + 1))
        vania_options.append(1 + game(s1, s2 * 2))
    vania_moves = min(vania_options) if vania_options else float('inf')

    # Возвращаем максимальное количество ходов, которые могут быть сделаны из текущей позиции
    return max(petia_moves, vania_moves)


# Проверяем для всех возможных начальных позиций (S1, S2), где 1 ≤ S1,S2 ≤ 69
max_moves = 0
max_positions = []
for s1 in range(1, 70):
    for s2 in range(1, 70):
        moves = game(s1, s2)
        if moves > max_moves:
            max_moves = moves
            max_positions = [(s1, s2)]
        elif moves == max_moves:
            max_positions.append((s1, s2))

# Выводим ответ
print("Максимальное количество ходов:", max_moves)
print("Начальные позиции с максимальным количеством ходов:")
for pos in max_positions:
    print(pos)
