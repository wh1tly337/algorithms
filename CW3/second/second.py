def main():
    with open('input.txt') as f:
        n = int(f.readline())
        words = []
        for i in range(n):
            word = list(f.readline().replace('\n', ''))
            word.sort()
            if word not in words:
                words.append(word)
        print(len(words))


if __name__ == '__main__':
    main()
