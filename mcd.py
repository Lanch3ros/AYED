def mcd(a, b):
    mcd_resultado = 1
    for div in range(2, min(a, b) + 1):
        if a % div == 0 and b % div == 0:
            mcd_resultado = div
    return mcd_resultado

print(mcd(2, 6))
print(mcd(6, 12))
print(mcd(200, 13))