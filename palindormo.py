'''
Estudiante: LANCHEROS AYORA JOSÉ LUIS

Determinar si una cadena S es un palindromo, un palindromo es aquella sucesión de caracteres en donde ci = cn-i para todo i > 0
input: 
              anitalavalatina
              ernesto
              a
              abalorio 
         
output: 
             True
             False
             True
             False
'''

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