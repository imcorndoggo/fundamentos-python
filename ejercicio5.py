'''
Clase:        Condicionales y operadores lógicos
Tema:         Condicionales y operadores lógicos
Ejercicio:     Número mágico
Descripción: Crea un programa en Python para determinar si un número es "mágico“.
Un número es “mágico” si es divisible por 7 pero no por 5.

Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
n=int(input("Ingrese un número: "))
if n%7==0 and n%5 !=0:
  print("El número es mágico")
else:
  print("El número no es mágico")