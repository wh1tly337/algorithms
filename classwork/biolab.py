def main():
    with open('27A.txt') as f:
        count_of_labs = int(f.readline())
        number_lab, count_prob = [], []
        for i in range(count_of_labs):
            [s1, s2] = f.readline().split(" ")
            number_lab.append(int(s1))
            count_prob.append((int(s2) - 1) // 36 + 1)

    # m = 1000 * number_lab[count_of_labs - 1] * count_of_labs
    # for i in range(count_of_labs):
    #     p = 0
    #     for j in range(count_of_labs):
    #         p += abs(number_lab[i] - number_lab[j]) * count_prob[j]
    #     m = min(m, p)
    #
    # print(m)

    result = []
    b = -sum(count_prob)
    for i in range(count_of_labs - 1):
        a = abs(number_lab[i] - number_lab[i + 1])
        b = b + (2 * count_prob[i])
        result.append(a * b)

    print(result)


if __name__ == '__main__':
    main()
