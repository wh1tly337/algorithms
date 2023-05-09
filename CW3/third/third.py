from math import sqrt


def main():
    with open('input.txt') as f:
        n = int(f.readline())
        for i in range(n):  # сложность O(n)
            number = int(f.readline())  # сложность O(n)
            radical = sqrt(number)  # сложность O(sqrt(number))
            if str(radical)[-2:] == '.0':
                if int(radical) ** 2 == number:
                    print(i + 1)


if __name__ == '__main__':
    main()

# Итог: сложность данного алгоритма  O(n * sqrt(number))
