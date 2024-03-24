def count_mines(matrix, i, j, rows, cols):
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1:
            count += 1

    return count


def mine_sweeper(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [['*' if matrix[i][j] == 1 else str(count_mines(matrix, i, j, rows, cols)) for j in range(cols)] for i in
              range(rows)]

    for row in result:
        print(' '.join(row))


if __name__ == "__main__":
    arr = []
    N = int(input("N: "))

    for i in range(N):
        mine_map = input(":")
        arr.append(list(map(int, mine_map.split())))

    mine_sweeper(arr)