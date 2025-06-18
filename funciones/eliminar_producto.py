# 7. Eliminar Productos
# De la lista original de productos que me permita eliminar un producto siempre y
# cuando el mismo no se encuentre registrado en una venta

def eliminar_productos(catalogo, ventas):
    productos = [item['descripción'] for item in catalogo]
    for idx in ventas:
        for fecha in ventas[idx]:
            for producto in productos:
                if producto not in ventas[idx][fecha]:
                    index = productos.index(producto)
                    del catalogo[index]

    return catalogo

