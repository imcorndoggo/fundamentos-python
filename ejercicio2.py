'''
Clase:        Variables, tipos, entradas y salidas
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Generador del correo de Key
Descripción:  Solicita al usuario su nombre completo (asume dos nombres y
dos apellidos). Luego, el programa generará, su correo con el
formato:
• primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
nombre=input("Ingrese sus nombre completo: ")
partes = nombre.strip().split()
primer_nombre = partes[0]
primer_apellido = partes[2]
correo = f"{primer_nombre.lower()}.{primer_apellido.lower()}@keyinstitute.edu.sv"
print(f"El correo que se debe asignar al usuario ingresado es:{correo}")