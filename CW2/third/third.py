def main():
    line = []
    with open('input.txt') as f:
        count_lines = int(f.readline())  # число команд
        for i in range(count_lines):
            element = f.readline().replace('\n', '')
            line.append(element)  # массив с записями
    mass = []
    for i in range(count_lines):
        action = line[i][0]  # получение действия
        if action == '+':
            mass.append(int(line[i].split(' ')[1]))  # добавление в массив
        elif action == '-':
            mass.remove(mass[0])  # удаление из массива
        else:
            result = merge_sort(mass)  # сортировка слиянием
            print(result[0])


# noinspection DuplicatedCode
def merge_sort(x):
    """Сортировка слиянием со сложностью O(N*log(N))."""
    # эта проверка значительно ускоряет процесс сортировки
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

# Итог: сложность данного алгоритма O(N*log(N), поскольку main() не обладает
# вложенными циклами или чем-то еще имеющим сложность больше O(N*log(N), а
# сортировка слиянием в любом случае имеет сложность O(N*log(N), что и является
# максимальной в данной программе. N - это количество записей в файле
