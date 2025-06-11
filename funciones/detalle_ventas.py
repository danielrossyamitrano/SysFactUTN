def mostrar_detalle_ventas(ventas, catalogo):
    # 6. Mostrar el detalle de todas las ventas con subtotales y total por factura.
    #  - Iterar sobre cada venta, buscar los datos del cliente y del producto, y calcular subtotales.
    for clnt in ventas:
        sub_t = 0
        for fecha in ventas[clnt]:
            prdct, cant = ventas[clnt][fecha]
            sub_t += [catalogo[i]["precio"] for i in range(len(catalogo))][0]
            print(f'{clnt} realizó un total de ventas igual a {cant} del producto "{prdct}" por un total de ${sub_t}\n')