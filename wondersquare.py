'''
Estudiante: LANCHEROS AYORA JOSÉ LUIS

Dado un número n, se deberá componer el WonderSquare de n, un WonderSquare de n se describe por la siguiente sucesión : 
1 -> 1

2 -> 2 2 2
     2 1 2
     2 2 2

3 -> 3 3 3 3 3 
     3 2 2 2 3
     3 2 1 2 3 
     3 2 2 2 3
     3 3 3 3 3

4 -> 
    4 4 4 4 4 4 4
    4 3 3 3 3 3 4
    4 3 2 2 2 3 4
    4 3 2 1 2 3 4
    4 3 2 2 2 3 4
    4 3 3 3 3 3 4
    4 4 4 4 4 4 4
'''

def distanceCell(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return max(abs(x0 - x1), abs(y0 - y1))

def wondersquare(n):
    dim = 2 * n - 1
    center = (n - 1, n - 1)
    mat = [[distanceCell((x, y), center) + 1 for x in range(dim)] for y in range(dim)]
    return mat

def printMat(mat):
    for row in mat:
        print(''.join(map(str, row)))

def pregunta ():
    n = int(input("\nIngrese el numero del wondersquare ---> "))
    print()
    if n < 1:
        print ("No es valido el numero ingresado")
    else:
        mat = wondersquare(n)
        printMat (mat)

pregunta ()