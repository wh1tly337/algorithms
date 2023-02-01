def main():
    # with open("input1.txt") as f:
    #     input_values = f.readline().split(' ')  # сложность O(n) поскольку split делает посимвольную обработку
    #
    # result = int(input_values[0]) / int(input_values[1])

    result = 500002 / 500001  # нужно сделать чтобы нули в начале не учитывались
    print(result)

    result = str(result).split('.')
    integer = result[0]
    fractional = result[1]
    memory = []
    for i in range(len(fractional) - 1):
        for j in range(i, len(fractional)):
            if fractional[i] == fractional[j] and fractional[i] not in memory:
                memory.append(fractional[i])
                break

    if len(fractional) / len(memory) >= 2:
        print(f"{integer}.(" + "".join(memory) + ")")
    else:
        print(f"{integer}.({fractional})")


if __name__ == '__main__':
    main()

# нужно прописать для каждого действия его сложность при помощи комментария
# в конце каждой программы нужно написать общий вывод - общую сложность
# результатом будет вордовский файл в который нужно вставлять код (со всеми комментариями), а не скрины, после кода общий вывод
