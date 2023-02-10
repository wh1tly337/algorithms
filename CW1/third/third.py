def main():
    with open('input.txt') as f:  # open - это функция встроенного в Python модуля io. Использование open считается операцией со сложностью O(1) не требующая сложных вычислений или операций
        input_dock = f.readlines()  # функция readlines имеет сложность O(N)
        count_of_values = int(input_dock[0])
        all_values = input_dock[1::]

    result, helper = 0, 0
    for i in range(count_of_values):
        helper += int(all_values[i])
        if helper < 0:
            helper = 0
        result = max(result, helper)
    # Временная сложность приведенного выше кода равна O(n), где n - количество элементов в all_values. Код перебирает каждый элемент в all_values и выполняет постоянный объем вычислений для
    # каждого элемента, поэтому общее время пропорционально количеству элементов.

    print('Максимальная_сумма_подмассива =', result)


if __name__ == '__main__':
    from datetime import datetime

    start_time = datetime.now()
    main()

    print(datetime.now() - start_time)

# Итого разобрав по отдельности каждый блок кода мы понимаем что общая сложность данного алгоритма является линейной или O(N)
