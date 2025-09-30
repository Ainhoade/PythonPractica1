# 1 Pedimos al usuario una lista de números separados por coma
entrada = input("Ingresa números separados por coma (por ejemplo: 4,5,6,7): ")

# 2 Convierte la entrada a lista de enteros.
numeros = [int(num.strip()) for num in entrada.split(",")]

# 3 Calcula y muestra: suma, promedio, máximo y mínimo usando funciones.
suma = sum(numeros)
promedio = sum(numeros) / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

# 4 Usa f-strings para mostrar los resultados con formato
print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")
