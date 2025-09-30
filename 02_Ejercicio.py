# 1 Crea una función saludar(nombre) que reciba un nombre y devuelva un saludo:
def saludar(nombre):
    return f"Hola {nombre}, ¡bienvenido!"

# 2 Crea una función calcular_imc(peso, altura) que devuelva el IMC usando la fórmula: IMC = peso / (altura^2)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 3 Llama a estas funciones con los datos ingresados en el ejercicio 1 y muestra los resultados.
    # Ejercicio 1 (pedir datos al usuario) 
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))

    # Llamadas a las funciones 
print(saludar(nombre))  # saludo personalizado
imc = calcular_imc(peso, altura)

    # Mostrar resultados
print(f"Tienes {edad} años, mides {altura} m y pesas {peso} kg.")
print(f"Tu IMC es: {imc:.2f}")
