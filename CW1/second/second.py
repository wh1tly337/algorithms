def main():
    with open('input2.txt') as f:  # open - это функция встроенного в Python модуля io. Использование open считается операцией со сложностью O(1) не требующая сложных вычислений или операций
        input_dock = f.readlines()  # функция readline имеет сложность O(N) поскольку она проходит один раз по длине строки
    count_of_stones = int(input_dock[0])
    all_stones = list(map(int, input_dock[1].split()))  # функции list, map, split имеют сложности O(N) поскольку они проходят один раз по длине строки
    close_result = sum(all_stones) // 2  # Временная сложность sum() равна O(n), где n - количество суммируемых элементов.
    # Это связано с тем, что sum() выполняет итерацию по всем элементам в итерируемой таблице и суммирует их, поэтому время, которое она занимает, прямо пропорционально количеству элементов в
    # итерируемой таблице.

    # Счетная сортировка со сложностью O(N)
    k = max(all_stones) + 1  # noqa
    count = [0] * k
    for i in all_stones:
        count[i] += 1
    j = 0
    for i in range(k):
        for _ in range(count[i]):
            all_stones[j] = i
            j += 1

    prefix_sum = [0] * (count_of_stones + 1)
    for i in range(1, count_of_stones + 1):
        prefix_sum[i] = prefix_sum[i - 1] + int(all_stones[i - 1])
    # Данный алгоритм префиксной суммы имеет сложность O(N), тк один цикл проходит по количеству камней и не использует дополнительных функций

    result = float('inf')
    for i in range(count_of_stones):
        if 10 >= close_result - prefix_sum[i] >= -10:
            target_sum = prefix_sum[count_of_stones] - prefix_sum[i]
            if prefix_sum[i] - target_sum < 0:
                temporary = target_sum - prefix_sum[i]
            else:
                temporary = prefix_sum[i] - target_sum
            if temporary < result and prefix_sum[i] - target_sum != 0:
                result = temporary
    # Временная сложность блока выше составляет O(n), где n - count_of_stones. Алгоритм использует один цикл for для перебора всех элементов массива prefix_sum и выполняет операции постоянного
    # времени для каждой итерации, поэтому общая временная сложность линейна.

    print(result)


if __name__ == '__main__':
    main()

# Итого разобрав по отдельности каждый блок кода мы понимаем что общая сложность данного алгоритма является линейной или O(N)
