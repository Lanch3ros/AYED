'''
Estudiante: LANCHEROS AYORA JOSÉ LUIS

Dada una cadena S, compuesta por caracteres :
                  c0, c1, c2 ...... cn
        Determinar aquel caracter ci el cual tiene el mayor número de repeticiones ( No necesariamente contiguas) dentro de S

        Casos de prueba: 
      
        Input:
        anitalavalatina
        ricardo01
        123456777777
        elementaleeeeergo
       
        Output: 
        a -> 6
        r -> 2
        7 -> 6
        e -> 8
'''
casos_de_prueba = ["anitalavalatina", "ricardo01", "123456777777", "elementaleeeeergo"]

def c_mas_repetido(cadena):
    repeticiones = {}
    for caracter in cadena:
        if caracter in repeticiones:
            repeticiones[caracter] += 1
        else:
            repeticiones[caracter] = 1
    c_mas_repetido = max(repeticiones, key=repeticiones.get)
    return c_mas_repetido, repeticiones[c_mas_repetido]
    
def resultado ():
    for caso in casos_de_prueba:
        caracter, repeticiones = c_mas_repetido(caso)
        print(f"\n{caracter} ---> {repeticiones}")

resultado ()