def main():
    with open('input.txt') as f:
        n, m, k = map(int, f.readline().split())
        standard = [list(map(int, f.readline().split())) for _ in range(n)]
        similar = [list(map(int, f.readline().split())) for _ in range(k)]

    [standard[i].sort() for i in range(n)]
    [similar[i].sort() for i in range(k)]

    for i in similar:
        print(1) if i in standard else print(0)


if __name__ == '__main__':
    main()
