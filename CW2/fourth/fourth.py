def main():
    with open('input.txt') as f:
        count_elements = int(f.readline())
        elements = f.readline().split(' ')

    stack = []
    for i in range(count_elements):
        try:
            stack.append(int(elements[i]))
        except Exception:
            a = stack.pop()
            b = stack.pop()
            if elements[i] == '+':
                stack.append(b + a)
            elif elements[i] == '-':
                stack.append(b - a)
            elif elements[i] == '*':
                stack.append(b * a)

    print(*stack)


if __name__ == '__main__':
    main()
