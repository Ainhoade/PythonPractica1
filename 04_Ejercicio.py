# 1 Modifica el ejercicio 1 para que la edad y altura se pidan en un bucle que repita hasta que se ingrese un número válido.
    # Pedimos el nombre directamente
nombre = input("Ingresa tu nombre: ")

# 2 Usa try/except para capturar errores si el usuario escribe algo que no sea un número int o float en cada caso.
    # Pedimos la edad con validación
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break  # Si se ingresa un número válido, salimos del bucle
    except ValueError:
        print("⚠️ Error: la edad debe ser un número entero. Intenta de nuevo.")

    # Pedimos la altura con validación
while True:
    try:
        altura = float(input("Ingresa tu altura en metros: "))
        break  # Si se ingresa un número válido, salimos del bucle
    except ValueError:
        print("⚠️ Error: la altura debe ser un número decimal (usa punto). Intenta de nuevo.")

    # Mostramos los datos ingresados
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# Mostramos los tipos de variables
print(f"El tipo de 'nombre' es: {type(nombre)}")
print(f"El tipo de 'edad' es: {type(edad)}")
print(f"El tipo de 'altura' es: {type(altura)}")

