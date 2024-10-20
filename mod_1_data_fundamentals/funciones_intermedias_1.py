#Archivo .py

#--------------------------------------------------------------------------------------------------
# 1. Actualizar valores en diccionarios y listas

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

# Cambiar el valor de 3 en matriz por 6
matriz[1][0] = 6  # Cambia 3 por 6
print("Lista 'Matriz' actualizada:", matriz)

# Cambiar el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"  # Cambia el nombre del primer cantante
print("Diccionario 'Cantantes' actualizada:", cantantes)

# Cambiar "Cancún" por "Monterrey" en ciudades
ciudades["México"][2] = "Monterrey"  # Cambia Cancún por Monterrey
print("Diccionario 'Ciudades' actualizada:", ciudades)

# Cambiar el valor de "latitud" en coordenadas
coordenadas[0]["latitud"] = 9.9355431  # Cambia la latitud
print("Diccionario 'Coordenadas' actualizada:", coordenadas)

#-------------------------------------------------------------------------------------------------

# 2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for diccionario in lista:
        # Crea una lista de pares clave-valor en el formato requerido
        salida = [f"{llave} - {valor}" for llave, valor in diccionario.items()]
        # Une los pares con una coma
        print(", ".join(salida))

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

#-------------------------------------------------------------------------------------------------

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamadas de ejemplo
print("Nombres:")
iterarDiccionario2("nombre", cantantes)

print("\nPaíses:")
iterarDiccionario2("pais", cantantes)

#-------------------------------------------------------------------------------------------------

# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        # Imprimir el tamaño de la lista y el nombre de la clave en mayúsculas
        print(f"{len(lista)} {clave.upper()}")
        # Imprimir los valores de la lista
        for valor in lista:
            print(valor)
        # Imprimir una línea en blanco para mayor claridad
        print()

# Ejemplo de uso
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)