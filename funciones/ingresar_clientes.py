from .elegir_provincia import elegir_provincia


def ingresar_cliente():
    # 1. Cargar un listado de clientes (nombre, ID, provincia).
    # - Utilizar una lista de diccionarios. Cada diccionario representa un cliente.
    # - Validar que el ID no se repita y que el nombre y provincia no estén vacíos.
    clientes = []
    numero_cliente = None
    while True:
        numero = input("Ingrese su número de cliente: ")
        if numero.isdigit():
            if int(numero) not in [cliente["ID"] for cliente in clientes]:
                numero_cliente = int(numero)
            else:
                print(f"El número ingresado '{numero}' ya existe.")
                continue

        print("\nIngrese el nombre y apellido del cliente")
        texto = input('> ')
        letras = texto.replace(' ', '')  # esto es porque los espacios no son considerados alfabéticos.
        letras = letras.replace(',', '')  # las comas tampoco son consideradas alfabéticas.
        clientes_existentes = [cliente['nombre'] for cliente in clientes]

        if letras.isalpha():
            words = [word.capitalize() for word in texto.replace(', ', ' ').split(' ')]
            # Capitalizamos cada una de las palabras.
            nombre = ' '.join(words)  # y luego las unimos.
            if nombre not in clientes_existentes:
                data = {'ID': numero_cliente, 'nombre': nombre, 'provincia': elegir_provincia()}
                clientes.append(data)
                print(f"Cliente ingresado correctamente con el ID: {data['ID']}")

        elif texto == '':
            if input('¿Desea salir? ').lower().endswith('s'):
                return clientes

        else:
            print('Ingrese un texto válido.')

    return clientes