from functools import lru_cache

counter_p, counter_v = 0, 0


def main():
    max_p, max_v = 0, 0  # максимальное кол-во ходов для победы Пети и Вани
    move_p, move_v = 0, 0  # за какое кол-во ходов
    for i in range(1, 101):
        # print(f"Нач. кол-во камней: {i} | "
        #       f"Имя победителя и кол-во ходов {game(i)}")
        result = game(i)
        result = result.split(' ')
        # формирование результатов
        if result[0] == 'P':
            if int(result[1]) > max_p:
                max_p = int(result[1])
                move_p = i
        else:
            if int(result[1]) > max_v:
                max_v = int(result[1])
                move_v = i

    if max_p == max_v:
        print(f"Петя победит за {max_p} ходов, начиная с {move_p} камней и "
              f"Ваня победит за {max_v} ходов, начиная с {move_v} камней")
    elif max_p > max_v:
        print(f"Петя победит за {max_p} ходов, начиная с {move_p} камней")
    else:
        print(f"Ваня победит за {max_v} ходов, начиная с {move_v} камней")


def meaning(a):
    """Функция отвечающая за всевозможные ходы в игре."""
    return (a + 1), (a * 3 - 1)


@lru_cache(None)  # декоратор сохраняющий результаты выполнения функции
def game(a):
    """Функция вычисляющая победителя, зависит от начального кол-ва камней."""
    global counter_p, counter_v

    if a > 150:
        return 'win'
    elif any(game(x) == 'win' for x in meaning(a)):
        return 'P 1'
    elif all(game(x) == 'P 1' for x in meaning(a)):
        return 'V 1'
    elif any(game(x) == 'V 1' for x in meaning(a)):
        return 'P 2'
    elif all(game(x) == 'P 2' or game(x) == 'P1' for x in meaning(a)):
        return 'V 2'
    else:
        if any((game(i) == 'win' or game(i)[0] == 'V') for i in meaning(a)):
            counter_p += 1
            return f"P {2 + counter_p}"
        elif all(game(i)[0] == 'P' for i in meaning(a)):
            counter_v += 1
            return f"V {2 + counter_v}"


if __name__ == '__main__':
    main()

# Итог: Трудно точно определить временную сложность, поскольку она зависит от
# рекурсивной функции game(). Однако точно можно сказать, что:
#
# Функция main() выполняет итерации в диапазоне от 1 до 100, поэтому ее
# временная сложность равна O(1).
#
# Функция meaning() возвращает два значения, поэтому она имеет постоянную
# временную сложность O(1).
#
# Функция game() использует запоминание с помощью декоратора lru_cache(),
# поэтому она позволяет избежать избыточных рекурсивных вызовов и повышает
# общую временную сложность функции.
#
# Наихудшая временная сложность функции game() варьируется примерно от O(N)
# до O(2 ^ a).
#
# В целом, временная сложность этого алгоритма определяется временной
# сложностью функции game(), которую трудно точно определить. Однако
# использование запоминания с помощью декоратора lru_cache() помогает уменьшить
# количество рекурсивных вызовов и повысить общую временную сложность.
