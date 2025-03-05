B = [1, 3, 2, 423, 4234, 2312, 12413, 12, 21, 41, 94, 4]

def insertion_sort(A):
    length = len(A)
    if length <= 1:
        print("El arreglo tiene un único elemento, ya está ordenado")
        return

    for i in range(1, length):
        key = A[i]  # Guardamos el valor actual
        j = i - 1
        while j >= 0 and key < A[j]:  # Comparamos con valores anteriores
            A[j + 1] = A[j]  # Movemos elementos hacia la derecha
            j -= 1
        A[j + 1] = key  # Insertamos el elemento en su posición correcta

insertion_sort(B)
print(B)


#pre: data is sorted
# el not in data
#pos: data contains el and data is sorted
def findSortedPlace(data, el):                         #Cost(Peor)    #times (Peor)  #Cost(Mejor)    #times(Mejor)
    index = 0                                          # c0              1               C0             1
    while index < len(data) and data[index] <= el:     # c1              n + 1           c1             1
        index+=1                                       # c2              n               c2             0
    return data[:index] + [el] + data[index:]          # c3              1               c3             1
                                                            # T(n) = O(n)                      T(n) = Ohm(1)
#pre : data is a set of comparable elements
#pos : data is sorted
def insertionSort(data):                                        #Cost(Peor)    #times (Peor)  #Cost(Mejor)    #times(Mejor)
    initial_index = 1                                           # C0               1                C0               1
    sorted_data = data[:initial_index]                          # C1               1                C1               1
    for index in range(initial_index, len(data)):               # C2               n                C2               n
        sorted_data = findSortedPlace(sorted_data, data[index]) # n                n-1               1               n-1
    return sorted_data                                          # C3               1                C3               1
                                                                      #T(n) = O(n^2)