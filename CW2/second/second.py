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

    result = []
    for i in range(count_entries):
        value = ''
        for j in range(count_parameters):
            element = []
            elem = line[i]
            value += str(elem[int(priority[j])])
        element.append(value)
        element.append(line[i][0])
        result.append(element)
    result.sort(reverse=True)
    for i in range(count_entries):
        print(result[i][1])


if __name__ == '__main__':
    main()
