def main():
    with open('input.txt') as f:
        n, m, k = map(int, f.readline().split())
        # составление массива начальных множеств O(n)
        standard = [list(map(int, f.readline().split())) for _ in range(n)]
        # составление массива множеств с которыми нужно работать (подобные)O(n)
        similar = [list(map(int, f.readline().split())) for _ in range(k)]

    # сортировка полученных ранее множеств O(n*m*log(n)),
    # тк сложность встроенной сортировки O(m*log(m))
    [standard[i].sort() for i in range(n)]
    [similar[i].sort() for i in range(k)]

    # Проверка есть ли у множества подобное O(n)
    for i in similar:
        print(1) if i in standard else print(0)


if __name__ == '__main__':
    main()

# Итог: сложность данного алгоритма O(n*log(n))
