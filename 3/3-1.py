"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permita
verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
"""

#a) Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.
def CargaManualMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for i in range(columnas):
            fila.append(int(input("Ingrese un numero: ")))
        print("\n")
        matriz.append(fila)
    return matriz

# b) Ordenar en forma ascendente cada una de las filas de la matriz.
def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux

def OrdenarCadaFila(matriz):
    for i in range(len(matriz)):
        # matriz[i] es una fila
        BubbleSort(matriz[i])
    
                
    

def ImpresoraMatriz(matriz):
    for f in range(len(matriz)):
        for c in range (len(matriz[f])):
            print(matriz[f][c], end="  ")
        print("\n")
        

#------------------------------------------------------------------------
m = CargaManualMatriz(2,4) # a)
OrdenarCadaFila(m)
ImpresoraMatriz(m) # b)
