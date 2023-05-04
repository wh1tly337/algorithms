from functools import lru_cache


def moves(s):
    a, b = s
    return (a * 2, b), (a + 1, b), (a, b * 2), (a, b + 1)


@lru_cache(None)
def game(s):
    if sum(s) >= 77:
        return 'end'
    elif any(game(x) == 'end' for x in moves(s)):
        return 'PETR1'
    elif all(game(x) == 'PETR1' for x in moves(s)):
        return 'IVAN1'
    elif any(game(x) == 'IVAN1' for x in moves(s)):
        return 'PETR2'
    elif all(game(x) == 'PETR1' or game(x) == 'PETR2' for x in moves(s)):
        return 'IVAN2'


for i in range(1, 69):
    j = 1
    while i + j < 77:
        heap = (j, i)
        print(i, j, game(heap))
        j += 1
