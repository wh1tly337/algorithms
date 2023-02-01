def main():
    with open('input2.txt') as f:
        input_dock = f.readlines()
    count_of_stones = int(input_dock[0])
    all_stones = input_dock[1].split(' ')

    sum_of_stones = 0
    for i in range(count_of_stones):
        sum_of_stones += int(all_stones[i])
    close_result = sum_of_stones // 2

    changed = True  # noqa
    while changed:
        changed = False
        for i in range(count_of_stones - 1):
            if all_stones[i] < all_stones[i + 1]:
                all_stones[i], all_stones[i + 1] = all_stones[i + 1], all_stones[i]
                changed = True

    try_close_result = 0
    sum_of_stones = 0
    result = 1000000000
    for i in range(count_of_stones):
        sum_of_stones += int(all_stones[i])
        if 2 >= close_result - sum_of_stones >= -2:
            for j in range(i + 1, count_of_stones):
                try_close_result += int(all_stones[j])

        if sum_of_stones - try_close_result < 0:
            temporary = try_close_result - sum_of_stones
        else:
            temporary = sum_of_stones - try_close_result

        if temporary < result and sum_of_stones - try_close_result != 0:
            result = temporary
    print(result)


if __name__ == '__main__':
    main()

    # input 1:
    # 0.03s
    # 18.0 MiB

    # input 2:
    # 0.03s
    # 18.1 MiB
