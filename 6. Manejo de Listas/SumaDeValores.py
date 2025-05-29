'''
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    Sumador de valores posicionales
Descripción: Pide un número al usuario y suma sus digitoss hasta que quede un solo digito.
Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''
numero = int(input("Ingrese un número: "))
def reducir_a_un_digito(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n
resultado = reducir_a_un_digito(numero)
print(f"El resultado de reducir a un solo dígito es: {resultado}")