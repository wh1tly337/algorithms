from functools import lru_cache

counter_p, counter_v = 0, 0


def main():
    max_p, max_v = 0, 0
    move_p, move_v = 0, 0
    for i in range(1, 101):
        result = game(i)
        result = result.split(' ')
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
    return (a + 1), (a * 3 - 1)


@lru_cache(None)
def game(a):
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
