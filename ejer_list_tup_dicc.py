# Lista de ventas
ventas = [
    {'fecha': '2024-01-01', 'producto': 'Producto A', 'cantidad': 10, 'precio': 5.0},
    {'fecha': '2024-01-01', 'producto': 'Producto B', 'cantidad': 5, 'precio': 7.5},
    {'fecha': '2024-01-02', 'producto': 'Producto A', 'cantidad': 8, 'precio': 5.0},
    {'fecha': '2024-01-02', 'producto': 'Producto C', 'cantidad': 3, 'precio': 10.0},
    {'fecha': '2024-01-03', 'producto': 'Producto B', 'cantidad': 2, 'precio': 8.0},
    {'fecha': '2024-01-03', 'producto': 'Producto B', 'cantidad': 2, 'precio': 9.5},
    {'fecha': '2024-01-03', 'producto': 'Producto A', 'cantidad': 5, 'precio': 6.0},
    {'fecha': '2024-01-04', 'producto': 'Producto C', 'cantidad': 6, 'precio': 7.6},
    {'fecha': '2024-01-04', 'producto': 'Producto A', 'cantidad': 5, 'precio': 5.2},
    {'fecha': '2024-01-05', 'producto': 'Producto C', 'cantidad': 2, 'precio': 6.5},
    {'fecha': '2024-01-05', 'producto': 'Producto B', 'cantidad': 3, 'precio': 5.5},
    {'fecha': '2024-01-06', 'producto': 'Producto C', 'cantidad': 2, 'precio': 7.0},
]
def iterarDiccionario(lista):
    for diccionario in lista:
        # Crea una lista de pares clave-valor en el formato requerido
        salida = [f"{llave}: {valor}" for llave, valor in diccionario.items()]
        # Une los pares con una coma
        print(" - ".join(salida))

iterarDiccionario(ventas)

#--------------------------------------------------------------------------------------------------
# 1. Cálculo de ingresos totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta['cantidad'] * venta['precio']
print(f"Ingresos totales: {ingresos_totales}")

#--------------------------------------------------------------------------------------------------
# 2. Análisis del producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta['producto']
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + venta['cantidad']

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]
print(f"Producto más vendido: {producto_mas_vendido} (Cantidad: {cantidad_mas_vendida})")

#--------------------------------------------------------------------------------------------------
# 3. Promedio de precio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta['producto']
    if producto not in precios_por_producto:
        precios_por_producto[producto] = (venta['precio'] * venta['cantidad'], venta['cantidad'])
    else:
        total_precio, total_cantidad = precios_por_producto[producto]
        precios_por_producto[producto] = (total_precio + venta['precio'] * venta['cantidad'], total_cantidad + venta['cantidad'])

for producto, (total_precio, total_cantidad) in precios_por_producto.items():
    precio_promedio = total_precio / total_cantidad
    print(f"Producto: {producto}, Precio promedio: {precio_promedio}")

#--------------------------------------------------------------------------------------------------
# 4. Ventas por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta['fecha']
    ingreso = venta['cantidad'] * venta['precio']
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

for fecha, ingreso in ingresos_por_dia.items():
    print(f"Fecha: {fecha}, Ingresos: {ingreso}")

#--------------------------------------------------------------------------------------------------
# 5. Resumen de ventas por producto
resumen_ventas = {}
for producto, total_cantidad in ventas_por_producto.items():
    total_ingreso = precios_por_producto[producto][0]
    precio_promedio = total_ingreso / total_cantidad
    resumen_ventas[producto] = {
        'cantidad_total': total_cantidad,
        'ingresos_totales': total_ingreso,
        'precio_promedio': precio_promedio
    }

print("\nResumen de ventas:")
for producto, datos in resumen_ventas.items():
    print(f"Producto: {producto}, Datos: {datos}")

#--------------------------------------------------------------------------------------------------
