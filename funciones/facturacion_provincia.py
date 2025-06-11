def facturacion_por_provincia(ventas, catalogo, clientes):
    # 9. Generar un resumen de facturación por provincia.
    # - Sumar las ventas agrupadas por provincia basándose en la provincia del cliente.
    ventas_provincia = {}
    for cliente, provincia in [[clientes[i]["nombre"], clientes[i]['provincia']] for i in range(len(clientes))]:
        if provincia not in ventas_provincia:
            ventas_provincia[provincia] = []
            if cliente in ventas:
                for fecha in ventas[cliente]:
                    item, cantidad = ventas[cliente][fecha]
                    redito = cantidad * [objeto["precio"] for objeto in catalogo if item == objeto["descripción"]][0]
                    ventas_provincia[provincia].append(redito)

    for provincia in ventas_provincia:
        print(f'{provincia}: ${sum(ventas_provincia[provincia])}')