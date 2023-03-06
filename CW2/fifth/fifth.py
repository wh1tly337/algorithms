from functools import lru_cache

counterP, counterV = 0, 0


def main():
    for i in range(1, 101):
        print(i, game(i), meaning(i))


def meaning(a):
    return (a + 1), (a * 3 - 1)


@lru_cache(None)
def game(a):
    global counterP, counterV

    if a > 150:
        return 'win'
    elif any(game(x) == 'win' for x in meaning(a)):
        return 'P1'
    elif all(game(x) == 'P1' for x in meaning(a)):
        return 'V1'
    elif any(game(x) == 'V1' for x in meaning(a)):
        return 'P2'
    elif all(game(x) == 'P2' or game(x) == 'P1' for x in meaning(a)):
        return 'V2'
    else:
        if any((game(i) == 'win' or game(i)[0] == 'V') for i in meaning(a)):
            counterP += 1
            return f"P{2 + counterP}"
        elif all(game(i)[0] == 'P' for i in meaning(a)):
            counterV += 1
            return f"V{2 + counterV}"


if __name__ == '__main__':
    main()
