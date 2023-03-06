def main():
    with open('input.txt') as f:
        count_elements = int(f.readline())
        elements = f.readline().split(' ')

    max_iter = 0
    for i in range(count_elements):
        try:
            int(elements[i])
        except Exception:
            max_iter += 1
            continue

    i, k = 0, 0
    while k < max_iter:
        symbol = False
        if elements[i] == '+':
            meaning = int(elements[i - 2]) + int(elements[i - 1])
            symbol = True
        elif elements[i] == '-':
            meaning = int(elements[i - 2]) - int(elements[i - 1])
            symbol = True
        elif elements[i] == '*':
            meaning = int(elements[i - 2]) * int(elements[i - 1])
            symbol = True
        else:
            i += 1

        if symbol:
            elements.remove(elements[i])
            elements.remove(elements[i - 1])
            elements[i - 2] = str(meaning)  # noqa
            k += 1
            i = 0

    print(*elements)


if __name__ == '__main__':
    main()
