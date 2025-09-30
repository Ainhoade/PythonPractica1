# 1 Instala la librería emoji en tu entorno virtual.
import emoji

# 2 Muestra un mensaje con un emoji usando la librería.
print(emoji.emojize("¡Bienvenido! :smile:", language="alias"))

def calcular_imc_con_emoji(peso, altura):
    imc = peso / (altura * 2)
    
    if imc < 18.5:
        estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
    elif imc < 25:
        estado = "Normal " + emoji.emojize(":smile:", language="alias")
    else:
        estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
    
    return imc, estado


# ---- Ejemplo de uso ----
peso = input("Ingresa tu peso en kg: "); float()
altura = input("Ingresa tu altura en metros: "); float()

imc, estado = calcular_imc_con_emoji(peso, altura)
print(f"Tu IMC es: {imc:.2f} → {estado}")