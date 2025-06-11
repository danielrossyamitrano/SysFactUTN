def productos_sin_ventas(ventas, catalogo):
    # 10. Listar productos sin ventas.
    # - Usar un set para registrar los códigos vendidos y luego filtrar los productos que no están en ese set.
    set_codigos_producto = set([str(objeto["código"]) for objeto in catalogo])
    productos_vendidos = set()
    for cliente in ventas:
        for fecha in ventas[cliente]:
            producto, _ = ventas[cliente][fecha]
            codigo = [objeto["código"] for objeto in catalogo if objeto['descripción'] == producto][0]
            productos_vendidos.add(str(codigo))

    print('Códigos de productos in vender: ' + ', '.join(set_codigos_producto.difference(productos_vendidos)) + '.')