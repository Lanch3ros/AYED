def es_palindromo(s):
    inicio = 0
    fin = len(s) - 1

    while inicio < fin:
        if s[inicio] != s[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

print(es_palindromo("anitalavalatina"))
print(es_palindromo("ernesto"))
print(es_palindromo("a"))
print(es_palindromo("abalorio"))