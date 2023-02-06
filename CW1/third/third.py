def main():
    with open('input.txt') as f:  # noqa
        input_dock = f.readlines()
        count_of_values = int(input_dock[0])
        all_values = input_dock[1::]

    result, helper = 0, 0
    for i in range(count_of_values):
        helper += int(all_values[i])
        if helper < 0:
            helper = 0
        result = max(result, helper)

    print('Максимальная_сумма_подмассива =', result)


if __name__ == '__main__':
    main()

    # 0.03s
    # 18.0 MiB
