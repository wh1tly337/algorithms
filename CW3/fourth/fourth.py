def main(matrix, row):
    if row == len(matrix):
        get_result(matrix)
        return

    for i in range(len(matrix)):
        if is_safe(matrix, row, i):
            matrix[row][i] = 'M'
            main(matrix, row + 1)
            matrix[row][i] = '–'
        else:
            main(matrix, row + 1)


def is_safe(matrix, row, column):
    horse = {
        '0': {'x': +2, 'y': +1},
        '1': {'x': +1, 'y': +2},
        '2': {'x': -1, 'y': +2},
        '3': {'x': -2, 'y': +1},
        '4': {'x': -2, 'y': -1},
        '5': {'x': -1, 'y': -2},
        '6': {'x': +1, 'y': -2},
        '7': {'x': +2, 'y': -1}
    }
    for i in range(7):
        try:
            move = horse.get(str(i))
            if matrix[row + move.get('x')][column + move.get('y')] == 'M':
                return False
        except Exception:
            continue

    for i in range(row):
        if matrix[i][column] == 'M':
            return False

    i, j = row, column
    while i >= 0 and j >= 0:
        if matrix[i][j] == 'M':
            return False
        i, j = i - 1, j - 1

    i, j = row, column
    while i >= 0 and j < len(matrix):
        if matrix[i][j] == 'M':
            return False
        i, j = i - 1, j + 1

    return True


def get_result(matrix):
    counter = 0
    for row in matrix:
        if 'M' in row:
            counter += 1
    if counter > 2:
        print(counter)
        for row in matrix:
            print(str(row).replace(',', '').replace('\'', ''))
        print()


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())

    main([['-'] * n for _ in range(n)], 0)
