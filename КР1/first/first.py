def creating_arrays():
    with open('input.txt') as f:  # noqa
        input_dock = f.readline().split(' ')

    a, b = [], []  # noqa
    for i in range(len(input_dock)):
        if input_dock[i] != '0':
            a.append(int(input_dock[i]))
        else:
            for j in range(i + 1, len(input_dock) - 1):
                b.append(int(input_dock[j]))
            break

    return a, b


def symmetric_difference(a, b):
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

    return result


def sorting(result):
    changed = True  # noqa
    while changed:
        changed = False
        for i in range(len(result) - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                changed = True
    print(*result)


if __name__ == '__main__':
    a, b = creating_arrays()
    result = symmetric_difference(a, b)
    sorting(result)
    # time python first.py - time usage
    # file for_looking_memory.py - RAM usage

    # 0.02s
    # 18.1 MiB
