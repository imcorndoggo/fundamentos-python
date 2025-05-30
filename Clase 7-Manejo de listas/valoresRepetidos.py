'''
Clase:        Clase 7
Tema:         Manejo de listas
Ejercicio:    Eliminando valores duplicados
Descripción: Dada una lista de números enteros, elimina los valores duplicados y muestra la lista resultante.
Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

entrada = input("Ingrese números separados por comas: ")
numeros = [int(x.strip()) for x in entrada.split(",")]
sin_duplicados = []
for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)
print("Lista sin duplicados:", sin_duplicados)