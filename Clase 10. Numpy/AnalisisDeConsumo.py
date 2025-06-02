'''
Clase:        Clase 10
Tema:         Numpy
Ejercicio:    Análisis de consumo de energía eléctrica
Descripción: Sigue las indicaciones.
Autor:        Andrea Nicole Herrera Cienfuegos
Fecha:        2025-06-02
Estado:       [ Terminado ]
'''

import numpy as np
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones:", consumo.ndim)
import numpy as np
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipos de datos:", consumo.dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miercoles(día 3)", consumo[:,2])

promedio_por_hogar = np.mean(consumo, axis=1)
promedio_por_dia = np.mean(consumo, axis=0)
total_consumo = np.sum(consumo)

print("Promedio por hogar:", promedio_por_hogar)
print("Promedio por día:", promedio_por_dia)
print("Total de consumo:", total_consumo)

maximo=np.max(consumo)
minimo=np.min(consumo)
desviacion=np.std(consumo)
print("Desviación estándar:", desviacion)
print("Máximo consumo:", maximo)
print("Mínimo consumo:", minimo)


consumo_total_hogar = np.sum(consumo, axis=1)
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
hogar_mas_eficiente = np.argmin(consumo_total_hogar)
print("Hogar con mayor consumo:", hogar_mayor_consumo)
print("Consumo total por hogar:", consumo_total_hogar)
print("Hogar más eficiente:", hogar_mas_eficiente)

consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

altos = consumo_total_hogar >100
consumo_mayor_100 = np.where(altos)[0]

print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

consumo_normalizado = (consumo - consumo.min())/(consumo.max() - consumo.min())
print(consumo_normalizado)



'''Preguntas'''

# 1. 
consumo_hogar5_viernes = consumo[4, 4]
print("1. Consumo del hogar 5 el viernes:", consumo_hogar5_viernes)

# 2. 
consumo_ultimos3_domingo = consumo[-3:, 6]
print("2. Consumo de los últimos 3 hogares el domingo:", consumo_ultimos3_domingo)

# 3.
promedio_finde = np.mean(consumo[:, [5, 6]])
print("3. Promedio de consumo en fines de semana:", promedio_finde)

# 4. 
desviacion_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviacion_por_dia)
print("4. Día con mayor desviación estándar:", dia_mayor_desviacion)
print("   Esto indica que el día", dia_mayor_desviacion, "es el día en que los consumos entre hogares fueron más variables,")
print("   es decir, hubo más diferencia entre los hogares ese día.")

# 5. 
consumo_total_por_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_por_hogar)[:3]
valores_menor_consumo = consumo_total_por_hogar[indices_menor_consumo]
print("5. Índices de los 3 hogares con menor consumo:", indices_menor_consumo)
print("   Valores de consumo total de esos hogares:", valores_menor_consumo)

# 6.
consumo_hogar3 = consumo[2]
consumo_hogar3_aumentado = consumo_hogar3 * 1.10
nuevo_total_hogar3 = np.sum(consumo_hogar3_aumentado)
print("6. Nuevo consumo total del hogar 3 con aumento del 10% diario:", nuevo_total_hogar3)
