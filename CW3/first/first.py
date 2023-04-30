def main():
    with open('input.txt') as f:
        n, m, k = map(int, f.readline().split())
        standard = [set(map(int, f.readline().split())) for _ in range(n)]
        similar = [set(map(int, f.readline().split())) for _ in range(k)]

    for i in similar:
        if i in standard:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    main()
