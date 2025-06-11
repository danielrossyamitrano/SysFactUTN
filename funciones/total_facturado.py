def total_facturado(ventas, catalogo):
    # 7. Calcular y mostrar el total facturado por cliente.
    # - Acumular el total de ventas por cliente utilizando un diccionario auxiliar.
    for clnt in ventas:
        sub_t = 0
        for fecha in ventas[clnt]:
            prdct, cant = ventas[clnt][fecha]
            sub_t += [catalogo[i]["precio"] for i in range(len(catalogo)) if catalogo[i]['descripción'] == prdct]
            print(f'{clnt} realizó un total de ventas por un total de ${sub_t}\n')