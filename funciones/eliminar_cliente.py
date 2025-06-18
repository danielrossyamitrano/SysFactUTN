# 8. Eliminar Cliente
# De la lista original de diccionario de Clientes que me permita eliminar un cliente siempre y
# cuando el mismo no se encuentre registrado en una venta

def eliminar_clientes(clientes: list, ventas:list):
    flagged = []
    for i, cliente in enumerate(clientes):
        idx = clientes['id']
        if not idx in ventas:
            flagged.append(i)
    for idx in flagged:
        clientes.remove(idx)

    return clientes
