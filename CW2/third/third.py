import operator


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
