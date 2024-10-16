matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# 1. Cambiar el valor de 3 en matriz por 6
matriz[1][0] = 6  # Cambia 3 por 6
print("Lista 'Matriz' actualizada:", matriz)

# 2. Cambiar el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"  # Cambia el nombre del primer cantante
print("Diccionario 'Cantantes' actualizada:", cantantes)

# 3. Cambiar "Cancún" por "Monterrey" en ciudades
ciudades["México"][2] = "Monterrey"  # Cambia Cancún por Monterrey
print("Diccionario 'Ciudades' actualizada:", ciudades)

# 4. Cambiar el valor de "latitud" en coordenadas
coordenadas[0]["latitud"] = 9.9355431  # Cambia la latitud
print("Diccionario 'Coordenadas' actualizada:", coordenadas)