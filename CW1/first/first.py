# from memory_profiler import profile
#
#
# @profile
def main():
    with open('input.txt') as f:
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

    # счетная сортировка со сложностью O(N)
    k = max(result) + 1
    count = [0] * k
    for i in result:
        count[i] += 1
    j = 0
    for i in range(k):
        for _ in range(count[i]):
            result[j] = i
            j += 1

    print(*result)


if __name__ == '__main__':
    main()
