def ingresar_ventas(clientes, catalogo, ventas=None):
    # 3. Registrar ventas realizadas.
    # - Representar cada venta como un diccionario con cliente (por ID), fecha, y una lista de tuplas (producto y cantidad).
    #  - Validar que el cliente exista, que los códigos de producto sean válidos, y que las cantidades sean mayores a cero.

    if ventas is None:
        ventas = {}
    while True:
        n_cliente = input('Ingrese sú número de cliente: ')
        if n_cliente.isdigit() and int(n_cliente) in [clnt['ID'] for clnt in clientes]:
            cliente = int(n_cliente)
            if cliente not in ventas:
                ventas[cliente] = {}
            print('Acceso concedido\n#########################\n\n')
            break
        else:
            print(f'El número de cliente ingresado [{n_cliente}] es inválido')

    while True:
        print("Elija el producto sobre el que se realizó la operación")
        for i, item in enumerate(catalogo):
            producto = item['descripción']
            print(f'{i}: {producto}')

        producto_elegido = input('> ')
        if producto_elegido.isdigit() and 0 <= int(producto_elegido) < len(catalogo):
            producto_elegido = catalogo[int(producto_elegido)]['descripción']
        else:
            print('El producto ingresado es inválido')

        cantidad = input('Ingrese la cantidad de ventas realizadas para este producto: ')
        if cantidad.isdigit() and int(cantidad) > 0:
            cantidad = int(cantidad)
        else:
            print('la cantidad debe ser un número natural mayor a 0')

        fecha = input('Ingrese la fecha de la operación: ')
        if any(['/' in fecha, '-' in fecha, '.' in fecha]):
            fecha = fecha.replace('-', '/').replace('.', '/')
        else:
            print('el formato de la fecha es inválido')

        ventas[cliente][fecha] = (producto_elegido, cantidad)

        if input('¿Desea salir? ').lower().endswith('s'):
            return ventas