def mostrar_listado(clientes, productos):
    # 4. Mostrar el listado completo de clientes y productos.
    # - Recorrer las listas de clientes y productos e imprimir cada elemento con formato legible.
    opciones = ['Mostrar clientes', "Mostrar productos", "Nada"]

    while True:
        print('Elija una opción')
        for i, opcion in enumerate(opciones):
            print(f'{i}: {opcion}')

        opcion = input('> ')
        if opcion.isdigit() and 0 <= int(opcion) < len(opciones):
            match int(opcion):
                case 0:
                    for cliente in clientes:
                        nombre = cliente['nombre']
                        provincia = cliente['provincia']
                        idx = cliente['ID']
                        print(f'Nombre: {nombre}, Provincia: {provincia}, Idenficación: #{idx}')
                case 1:
                    for item in productos:
                        nombre = item['descripción']
                        precio = item['precio']
                        print(f'Nombre: {nombre}, Precio: ${precio}')
                case 2:
                    break
                case _:
                    print('Opción inválida')