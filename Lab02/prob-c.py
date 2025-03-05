from sys import stdin

def is_power_of_two(n):
    return (n & (n - 1)) == 0 and n > 0

def hadamard_check(matrix, n):
    for i in range(n - 1):
        diff_count = sum(matrix[i][j] != matrix[i + 1][j] for j in range(n))
        if diff_count != n // 2:
            return "No Hadamard"
    return "Hadamard"

def main():
    n = int(stdin.readline().strip())
    if n == 1: 
        return print("Hadamard" if stdin.readline().strip() == "T" else "No Hadamard")
    if not is_power_of_two(n):
        return print("Imposible")
    elements = stdin.readline().strip().split()
    matrix = [[elements[i * n + j] == 'T' for j in range(n)] for i in range(n)]    
    print(hadamard_check(matrix, n))

main()
