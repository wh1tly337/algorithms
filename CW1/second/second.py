def main():
    with open('input1.txt') as f:
        input_dock = f.readlines()
    count_of_stones = int(input_dock[0])
    all_stones = list(map(int, input_dock[1].split()))
    close_result = sum(all_stones) // 2

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

    result = float('inf')
    for i in range(count_of_stones):
        if 2 >= close_result - prefix_sum[i] >= -2:
            target_sum = prefix_sum[count_of_stones] - prefix_sum[i]
            if prefix_sum[i] - target_sum < 0:
                temporary = target_sum - prefix_sum[i]
            else:
                temporary = prefix_sum[i] - target_sum
            if temporary < result and prefix_sum[i] - target_sum != 0:
                result = temporary

    print(result)


if __name__ == '__main__':
    main()
