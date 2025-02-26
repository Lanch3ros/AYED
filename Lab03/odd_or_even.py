from sys import stdin

def cycle_lenght(n):
    ct = 1
    while n != 1:
        if n % 2 != 0:
            n = (3 * n) + 1
        else:
            n //= 2
        ct += 1 
    return ct

def main():
    line = stdin.readline().strip()
    while line:
        n1, n2 = map(int, line.split())
        n3 = n1
        n4 = n2
        if n1 > n2:
            n1, n2 = n2, n1
        max_cycle = 0   
        for i in range(n1, n2 + 1):  
            cycle = cycle_lenght(i)
            if cycle > max_cycle:
                max_cycle = cycle  
        print(n3, n4, max_cycle)  
        line = stdin.readline().strip()
main()
