'''
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    ¡Adivina el número!
Descripción: Genera un número aleatorio entre 1 y 100 y pide al usuario que adivine el número.
El programa debe seguir pidiendo números hasta que el usuario adivine correctamente.
En cada intento, el programa debe informar si el número a adivinar es mayor o menor que el ingresado.
Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''
import random

numero_secreto=random.randint(1, 100)
while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print("¡Felicidades! Adivinaste el número.")
        break