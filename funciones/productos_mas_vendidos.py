def productos_mas_vendidos(ventas, catalogo):
    # 8. Mostrar los productos más vendidos (por cantidad total).
    #  - Usar un diccionario para contar cuántas unidades se vendieron de cada producto y ordenarlo.
    productos = [catalogo[i]['descripción'] for i in range(len(catalogo))]
    vendidos = {}
    for prd in productos:
        sub = (sum([ventas[clnt][fch][1] for clnt in ventas for fch in ventas[clnt] if ventas[clnt][fch][0] == prd]))
        vendidos[prd] = sub

    print("Los prodcutos más vendidos son: ")
    for key in sorted(vendidos.keys(), key=lambda e: vendidos[e], reverse=True):
        print(f'{key} con un total de {vendidos[key]} ventas')