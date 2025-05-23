'''
Clase:        Condicionales y operadores lógicos
Tema:         Condicionales y operadores lógicos
Ejercicio:    Año bisiesto
Descripción: Determina si un año es bisiesto, considerando las reglas gregorianas. 
Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
año=int(input("Ingrese un año: "))
if año%4==0 and año%100!=0 or año%400==0:
  print("El año es bisiesto")
else:
  print("El año no es bisiesto")
