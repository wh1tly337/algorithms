from functools import lru_cache


# noinspection PyShadowingNames
@lru_cache(None)
def max_moves(s1, s2):
    memo = {}

    # noinspection PyShadowingNames
    @lru_cache(None)
    def recurse(s1, s2, player):
        if s1 + s2 >= 77:
            return 0

        if (s1, s2, player) in memo:
            return memo[(s1, s2, player)]

        if player == 1:
            moves = []
            if s1 < 69:
                moves.append(recurse(s1 + 1, s2, 2))
            if s2 < 69:
                moves.append(recurse(s1, s2 + 1, 2))
            if s1 > 0:
                moves.append(recurse(2 * s1, s2, 2))
            if s2 > 0:
                moves.append(recurse(s1, 2 * s2, 2))
            result = 1 + min(moves)
        else:
            moves = []
            if s1 < 69:
                moves.append(recurse(s1 + 1, s2, 1))
            if s2 < 69:
                moves.append(recurse(s1, s2 + 1, 1))
            if s1 > 0:
                moves.append(recurse(2 * s1, s2, 1))
            if s2 > 0:
                moves.append(recurse(s1, 2 * s2, 1))
            result = 1 + max(moves)

        memo[(s1, s2, player)] = result
        return result

    max_moves = recurse(s1, s2, 1)
    return max_moves


def main():
    m = 0
    for i in range(1, 69):
        j = 1
        while i + j < 77:
            result = max_moves(j, i)
            if result > m:
                m = result
                pos = [i, j]
            j += 1

    # noinspection PyUnboundLocalVariable
    print(pos[0], pos[1], m)


if __name__ == '__main__':
    main()
