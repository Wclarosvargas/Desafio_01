#Desafío, implementación de una matriz para calificaciones
import random

#Funciones a implementar
#Mostrar_matriz

def mostrar_matriz(matriz,estudiantes,materias):
    print("    ",end=" ") #Acomoda los nombres de las materias, alejados de los nombress
    for materia in materias:
        print(materia, end=" ")
    print() #Hace un salto de linea 

    i=0    #Nos sirve como un contador, ingresar a cada valor del estudiante
    for estudiante in estudiantes: 
        print(estudiante, end=" ") # Impresión de los nombres de los estudiantes
        for calificacion in matriz[i]:
            print(calificacion, end=" ") #Impresión de calificaciones
        print()
        i +=1

def calcular_promedio_estudiantes(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma_total = 0
    suma_filas = [0]*filas

    for i in range(filas):
        for j in range(columnas):
            suma_total += matriz[i][j]
            suma_filas[i] += matriz[i][j]

    promedio = [suma / columnas for suma in suma_filas]
    return promedio

#Programa principal

estudiantes = ["juan","lisy","martin","joaco"]

materias = ["M1","I2","L4","P9","T8"]

n = len(estudiantes)
m = len(materias)
matriznxm = []
for fil in range(n):
    matriznxm.append([])
    for col in range(m):
        matriznxm[fil].append(random.randint(1,10))

mostrar_matriz(matriznxm,estudiantes,materias) #Llamado de función mostrar_matriz
promedio = calcular_promedio_estudiantes(matriznxm)
print("Promedio de cada estudiante", promedio)