'''
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

def caracter_mas_repetido(cadena):
    # Inicializar un diccionario vacío
    repeticiones = {}

    # Recorrer cada caracter de la cadena
    for caracter in cadena:
        # Si el caracter ya está en el diccionario, incrementar su conteo
        if caracter in repeticiones:
            repeticiones[caracter] += 1
        # Si el caracter no está en el diccionario, agregarlo con un conteo de 1
        else:
            repeticiones[caracter] = 1

    # Encontrar el caracter con el mayor número de repeticiones
    caracter_mas_repetido = max(repeticiones, key=repeticiones.get)

    # Devolver el caracter y su número de repeticiones
    return caracter_mas_repetido, repeticiones[caracter_mas_repetido]


# Casos de prueba
casos_de_prueba = [
    "anitalavalatina",
    "ricardo01",
    "123456777777",
    "elementaleeeeergo"
]

for caso in casos_de_prueba:
    caracter, repeticiones = caracter_mas_repetido(caso)
    print(f"{caracter} -> {repeticiones}")
