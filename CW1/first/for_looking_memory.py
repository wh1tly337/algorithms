from memory_profiler import profile


@profile
def main():
    with open('/Users/user/PycharmProjects/algorithms/first/input.txt') as f:
        input_dock = f.readline().split(' ')

    a, b = [], []  # noqa
    for i in range(len(input_dock)):
        if input_dock[i] != '0':
            a.append(int(input_dock[i]))
        else:
            for j in range(i + 1, len(input_dock) - 1):
                b.append(int(input_dock[j]))
            break

    result, memory = [], []  # noqa
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                memory.append(a[i])
                break
    for i in range(len(a)):
        if a[i] not in memory:
            result.append(a[i])
        if i < len(b):
            if b[i] not in memory:
                result.append(b[i])

    swapped = True  # noqa
    while swapped:
        swapped = False
        for i in range(len(result) - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
    print(*result)


if __name__ == '__main__':
    main()
