def main():
    money = [10, 50, 100, 200, 500, 1000, 2000, 5000]
    # what_need = int(input())
    what_need = 12740
    result = []
    num = -1
    while what_need != 0:
        if what_need - money[num] >= 0:
            what_need -= money[num]
            result.append(money[num])
        else:
            num -= 1

    print(result)


if __name__ == '__main__':
    main()
