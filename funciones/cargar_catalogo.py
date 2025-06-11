def cargar_catalogo():
    # 2. Cargar un catálogo de productos (código, descripción, precio).
    # - Utilizar una lista de diccionarios. Cada producto debe tener un código único.
    # - Validar que el código no exista previamente y que el precio sea mayor a cero.
    catalogo = []
    while True:
        producto = input('Ingrese el nombre del producto, o toque [Enter] para salir: ')
        if producto.replace(' ', '').isalpha():
            precio = input('Ingrese el precio del producto: ')
            if precio.replace('$', '').isdigit() and int(precio) > 0:
                codigo = input("Ingrese el código del producto: ")
                if codigo.isdigit():
                    catalogo.append({'descripción': producto, 'código': int(codigo), 'precio': int(precio)})
                else:
                    print("El código debe ser un número")
            else:
                print('El precio debe ser un número natural mayor a 0')
        elif producto == '':
            if input('\n¿Desea salir? ').lower().endswith('s'):
                return catalogo
        else:
            print('El nombre del producto ingresado es inválido')