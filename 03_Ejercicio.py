# 1 Crea una función presentar_persona(nombre="Usuario", edad=None, *aficiones) que muestre un mensaje
def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    # Mensaje base según si la edad está o no
    if edad is not None:
        mensaje = f"{nombre} tiene {edad} años"
    else:
        mensaje = f"{nombre} no indicó su edad"

    # Agregamos aficiones si las hay
    if aficiones:
        mensaje += " y le gusta: " + ", ".join(aficiones)

    print(mensaje)

# 2 Prueba la función con diferentes números de aficiones
presentar_persona("Ana", 25, "leer", "correr", "viajar")

# 3 Dale un valor por defecto al parámetro nombre para cuando no se pase ninguno.
presentar_persona()  # Usando nombre por defecto que lo asigna al principio de la función como "Usuario"


# Ejemplos adicionales
presentar_persona("Carlos", 30, "programar")
presentar_persona("Lucía", 18)
presentar_persona("Miguel")  # Sin edad ni aficiones
