del len
'''
Clase:        Condicionales y operadores lógicos
Tema:         Condicionales y operadores lógicos
Ejercicio:    Contraseña segura
Descripción: Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
mayúscula.

Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

contra=input("Ingrese una contraseña: ")
mayus=any(c.isupper()for c in contra)
num=any(c.isdigit()for c in contra)
longitud_valida = len(contra) >= 8
if mayus and num and longitud_valida:
  print("Contraseña segura")
else:
  print("Contraseña insegura")