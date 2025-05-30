'''
Clase:        Clase 7
Tema:         Manejo de listas
Ejercicio:    Números líderes
Descripción: Dada una lista de números, imprime todos los que son líderes
Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

entrada = input("Ingrese una lista de números separados por comas: ")
lista = [int(x.strip()) for x in entrada.split(",")]
lideres = []
max_derecha = float('-inf')
for num in reversed(lista):
    if num > max_derecha:
        lideres.append(num)
        max_derecha = num
lideres.reverse()
print("Números líderes:", lideres)