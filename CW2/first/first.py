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
