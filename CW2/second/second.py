def main():
    line, element = [], []
    with open('input.txt') as f:
        first_line = f.readline().split(' ')
        count_entries = int(first_line[0])
        count_parameters = int(first_line[1])
        priority = f.readline().replace('\n', '').split(' ')
        for i in range(count_entries):
            element = f.readline().replace('\n', '').split(' ')
            line.append(element)

    # Изначальный вариант (сложность O(N^2))
    # result = []
    # for i in range(count_entries):
    #     value = ''
    #     for j in range(count_parameters):
    #         element = []
    #         elem = line[i]
    #         value += str(elem[int(priority[j])])
    #     element.append(value)
    #     element.append(line[i][0])
    #     result.append(element)

    # Улучшенный вариант (если я все правильно понимаю, то сложность O(N))
    result = [
        [str(line[i][int(priority[j])]) for j in range(count_parameters)] +
        [line[i][0]] for i in range(count_entries)
    ]

    result = merge_sort(result)

    for i in range(count_entries - 1, -1, -1):
        print(result[i][-1])


# noinspection DuplicatedCode
def merge_sort(x):
    if len(x) < 20:
        return sorted(x)
    result = []
    mid = int(len(x) / 2)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    i, j = 0, 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


if __name__ == '__main__':
    main()
