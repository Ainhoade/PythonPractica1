# 1 Pide al usuario su nombre, edad y altura en metros
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))

# 2 Muestra un mensaje usando f-string con los datos ingresados
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# 3 Muestra el tipo de dato de cada variable
print(f"El tipo de 'nombre' es: {type(nombre)}")
print(f"El tipo de 'edad' es: {type(edad)}")
print(f"El tipo de 'altura' es: {type(altura)}")
