def main():
    line = []
    with open('input.txt') as f:
        count_lines = int(f.readline())
        for i in range(count_lines):
            element = f.readline().replace('\n', '')
            line.append(element)
    mass = []
    for i in range(count_lines):
        action = line[i][0]
        if action == '+':
            mass.append(int(line[i].split(' ')[1]))
        elif action == '-':
            mass.remove(mass[0])
        else:
            result = merge_sort(mass)
            print(result[0])


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
