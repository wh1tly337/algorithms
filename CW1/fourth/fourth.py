def main():
    with open("input2.txt") as f:  # open - это функция встроенного в Python модуля io. Использование open считается операцией со сложностью O(1) не требующая сложных вычислений или операций
        input_values = f.readline().split(' ')  # функции readline и split имеют сложности O(N) поскольку они оба проходят один раз по длине строки

    result = int(input_values[0]) / int(input_values[1])

    integer, fractional = str(result).split('.')  # функция split имеет сложность O(N) поскольку она проходит один раз по длине строки
    memory = []
    repeat = ""
    index = 0
    max_zeros, ind_zeros = 0, 0  # считает нули в начале
    while index < len(fractional):
        if (fractional[index] in memory) and (fractional[index + 1] in memory):
            repeat = fractional[:index]
            if (len(repeat) - max_zeros) >= (len(fractional) // 2):
                repeat = fractional
            break

        if fractional[index] != '0':
            memory.append(fractional[index])
        else:
            if index == ind_zeros:
                max_zeros += 1
                ind_zeros += 1
        index += 1
    # Временная сложность блока кода выше составляет O(n), где n - длина fractional. Это связано с тем, что код состоит из одного цикла, который итерирует дробную строку по одному символу за раз,
    # а объем работы, выполняемой внутри цикла, постоянен, поэтому временная сложность линейна по отношению к размеру входных данных.

    if repeat:
        print(f"{integer}.({repeat})")
    else:
        print(f"{integer}.{fractional}")


if __name__ == '__main__':
    main()

# Итого разобрав по отдельности каждый блок кода мы понимаем что общая сложность данного алгоритма является линейной или O(N)
