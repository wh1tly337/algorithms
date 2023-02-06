def main():
    with open("input2.txt") as f:
        input_values = f.readline().split(' ')  # сложность O(n) поскольку split делает посимвольную обработку

    result = int(input_values[0]) / int(input_values[1])

    # result = 500002 / 500001
    integer, fractional = str(result).split('.')
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

    if repeat:
        print(f"{integer}.({repeat})")
    else:
        print(f"{integer}.{fractional}")


if __name__ == '__main__':
    main()

# нужно прописать для каждого действия его сложность при помощи комментария
# в конце каждой программы нужно написать общий вывод - общую сложность
# результатом будет вордовский файл в который нужно вставлять код (со всеми комментариями), а не скрины, после кода общий вывод
