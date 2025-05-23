'''
Clase:        Variables, tipos, entradas y salidas
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Automatizando el cálculo de la propina
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
(por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
a pagar, sin menú.

Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-15
Estado:       [Terminado ]
'''

total_cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje = float(input("Ingrese el porcentaje de propina: "))
propina = total_cuenta * (porcentaje / 100)
total_final = total_cuenta + propina
print(f"Total de la cuenta: ${total_cuenta:.2f}")
print(f"Propina: ${propina:.2f}")
print(f"Total de la cuenta con propina ({porcentaje:}%): ${total_final:}")