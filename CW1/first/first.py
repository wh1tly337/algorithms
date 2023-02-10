def main():
    with open('input.txt') as f:  # open - это функция встроенного в Python модуля io. Использование open считается операцией со сложностью O(1) не требующая сложных вычислений или операций
        input_dock = f.readline().split(' ')  # функции readline и split имеют сложности O(N) поскольку они оба проходят один раз по длине строки

    a, b = [], []  # noqa
    for i in range(len(input_dock)):
        if input_dock[i] != '0':
            a.append(int(input_dock[i]))
        else:
            for j in range(i + 1, len(input_dock) - 1):
                b.append(int(input_dock[j]))
            break
    # Сложность кода составляет O(N), где N - длина списка input_dock.
    # В первом цикле, for i in range(len(input_dock)), перебирается список input_dock, поэтому временная сложность первого цикла равна O(N).
    # Во втором цикле, for j in range(i + 1, len(input_dock) - 1), снова проходим по списку input_dock, но начиная с i + 1, поэтому временная сложность второго цикла равна O(N).
    # Таким образом, общая временная сложность этого кода равна O(N).

    result, memory = [], set()
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and a[i] not in memory:
                memory.add(a[i])
                break
    # Временная сложность приведенного выше кода равна O(N), поскольку  использование set() для хранения элементов "памяти" позволяет осуществлять поиск элементов в наборе с постоянным временем,
    # вместо линейного времени при использовании списка.

    if len(a) == 0 or len(b) == 0:
        result = 0
        print(result)
    else:
        memory = set(memory)
        for i in range(len(a)):
            if a[i] not in memory:
                result.append(a[i])
            if i < len(b) and b[i] not in memory:
                result.append(b[i])
        # Сложность блока выше равна O(N) поскольку не имеет вложенных циклов и строка проходится всего один раз

        # Счетная сортировка со сложностью O(N)
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

# Итого разобрав по отдельности каждый блок кода мы понимаем что общая сложность данного алгоритма является линейной или O(N)
