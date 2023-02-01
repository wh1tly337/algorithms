def main():
    with open('input.txt') as f:  # noqa
        input_dock = f.readlines()
        count_of_values = int(input_dock[0])
        all_values = input_dock[1::]

    result = 0
    for i in range(count_of_values):
        cycle_result = 0
        helper = 0
        for j in range(i, count_of_values):
            if helper + int(all_values[j]) > cycle_result:
                helper += int(all_values[j])
                cycle_result = helper
            else:
                break
        if cycle_result > result:
            result = cycle_result

    print('Максимальная_сумма_подмассива =', result)


if __name__ == '__main__':
    main()

    # 0.03s
    # 18.0 MiB
