'''
Clase:        Condicionales y operadores lógicos
Tema:         Condicionales y operadores lógicos
Ejercicio:     Cálculo de impuesto
Descripción: Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
un usuario por el consumo de energía

Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
uni=int(input("Ingrese unidades consumidas: "))
if uni <=100:
  impuesto=0
elif uni <=200:
  impuesto=uni*0.5
else:
  impuesto=uni*0.7
print(f"El impuesto a pagar es de: ${impuesto}")