#Desafío, implementación de una matriz para calificaciones
import random

#Funciones a implementar
#Mostrar_matriz

def mostrar_matriz(matriz,estudiantes,materias):
    print('Calificaciones de los estudiantes:')
    print("Alumno    ",end=" ") #Acomoda los nombres de las materias, alejados de los nombress
    for materia in materias:
        print(f'{materia:>10}',end="") #Alinea las materias a la derecha
    print() #Hace un salto de linea 
    print('-'*60)

    i=0    #Nos sirve como un contador, ingresar a cada valor del estudiante
    for estudiante in estudiantes: 
        print(f'{estudiante:>8}',end="") # Alinea el nombre de estudiante
        for calificacion in matriz[i]:
            print(f'{calificacion:>10}',end="") #Alinea las calificaciones
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

    promedio_estudiantes = {}
    for i in range(filas):
        promedio_estudiantes[f'Estudiante {i+1}'] = suma_filas[i] / (columnas-1)

    return promedio_estudiantes

def calcular_promedio_materias(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma_columnas = [0]*columnas

    for i in range(filas):
        for j in range(columnas):
            suma_columnas[j] += matriz[i][j]
    
    promedio_materias = {}
    for i in range(columnas):
        promedio_materias[f"Materia {i+1}"] = suma_columnas[i] / filas

    return promedio_materias

#Programa principal

materias = ["Mate1","Ingles2","Lengua4","Psico9","Taller8"]
estudiantes = ["juan","lisy","martin","joaco"]


n = len(estudiantes)
m = len(materias)
matriznxm = []
for fil in range(n):
    matriznxm.append([])
    for col in range(m):
        matriznxm[fil].append(random.randint(1,10))

mostrar_matriz(matriznxm,estudiantes,materias) #Llamado de función mostrar_matriz

promedio_estudiante = calcular_promedio_estudiantes(matriznxm)
print("Promedio de cada estudiante")
for estudiante in promedio_estudiante:
    promedio = promedio_estudiante[estudiante]
    print(f'{estudiante}:{promedio:.2f}')

promedio_materias = calcular_promedio_materias(matriznxm)
print('Promedio de cada materia')
for materia in promedio_materias: #Itera sobre las materia de la promedio_materias
    promedio = promedio_materias[materia]
    print(f'{materia}:{promedio:.2f}')