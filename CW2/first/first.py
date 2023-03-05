import operator


def main():
    input_value = []
    with open('input.txt') as f:
        count = int(f.readline())
        for i in range(count):
            input_value.append(int(f.readline().replace('\n', '')))
    sorted_mass = merge_sort(input_value)
    three_plus, three_minus = 1, 1
    for i in range(1, 4):
        three_plus = three_plus * sorted_mass[-i]
    for i in range(3):
        if i < 2:
            three_minus = three_minus * sorted_mass[i]
        else:
            three_minus = three_minus * sorted_mass[-1]
    if three_plus > three_minus:
        print(three_plus)
    else:
        print(three_minus)


def merge_sort(line, compare=operator.lt):
    if len(line) < 2:
        return line[:]
    else:
        middle = int(len(line) / 2)
        left = merge_sort(line[:middle], compare)
        right = merge_sort(line[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


if __name__ == '__main__':
    main()
