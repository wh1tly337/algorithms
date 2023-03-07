def main():
    with open('input.txt') as f:
        count_elements = int(f.readline())  # количество записей
        elements = f.readline().split(' ')  # массив с записями

    stack = []
    for i in range(count_elements):
        try:
            # Проверка на то, является ли элемент массива числом или нет. Если
            # да, то добавляется в массив, если нет, то код уходит в except
            stack.append(int(elements[i]))
        except Exception:
            a = stack.pop()  # удаление элемента, над которым произвели вычисление
            b = stack.pop()  # удаление элемента, над которым произвели вычисление
            # вычисление результата и добавление его в массив
            if elements[i] == '+':
                stack.append(b + a)
            elif elements[i] == '-':
                stack.append(b - a)
            elif elements[i] == '*':
                stack.append(b * a)

    print(*stack)


if __name__ == '__main__':
    main()

# Итог: сложность данного алгоритма O(N), поскольку main() не обладает
# вложенными циклами или чем-то еще имеющим сложность больше O(N). N - это
# количество записей в файле
