from sys import stdin

def power_sum(X, N, num=1):
    power = num ** N
    if power > X:
        return 0    
    if power == X:
        return 1
    return power_sum(X - power, N, num + 1) + power_sum(X, N, num + 1)

def main ():
    X = int(stdin.readline())
    N = int(stdin.readline())
    R = power_sum(X, N)
    print(R)

main()