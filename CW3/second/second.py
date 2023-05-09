def main():
    words = set()  # сложность O(1)
    with open('input.txt') as f:
        n = int(f.readline())
        for i in range(n):  # сложность O(n)
            word = f.readline().strip()
            sorted_word = ''.join(sorted(word))  # сложность O(n*log(n))
            words.add(sorted_word)  # сложность O(1)
        print(len(words))


if __name__ == '__main__':
    main()

# Итог: сложность данного алгоритма O(n*log(n))
