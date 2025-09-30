import sys


def main():
    # Comprobamos número de argumentos
    if len(sys.argv) != 4:
        print("❌ Error: número de argumentos incorrecto.")
        return
    
    num1_str, operador, num2_str = sys.argv[1], sys.argv[2], sys.argv[3]

    # Intentamos convertir a números
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("⚠️ Error: los operandos deben ser números.")
        return

    # Operaciones soportadas
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("🚫 Error: no se puede dividir entre cero.")
            return
        resultado = num1 / num2
    else:
        print(f"⚠️ Operador '{operador}' no reconocido. Usa +, -, * o /.")
        return

    # Mostrar resultado
    print(f"✅ Resultado: {num1} {operador} {num2} = {resultado}")

if __name__ == "__main__":
    main()
