from sys import stdin

def generate_minesweeper_field(n, m, field):
    result = [[0] * m for _ in range(n)]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                result[i][j] = '*'
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and result[ni][nj] != '*':
                        result[ni][nj] += 1
    return [''.join(str(cell) for cell in row) for row in result]

def main():
    case_number = 0
    first_case = True
    while True:
        line = stdin.readline().strip()
        if not line:
            break
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        case_number += 1
        field = [stdin.readline().strip() for _ in range(n)]
        if not first_case:
            print()
        first_case = False
        print(f"Field #{case_number}:")
        for row in generate_minesweeper_field(n, m, field):
            print(row)
main()