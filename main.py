from funciones import *
from os import path, getcwd, mkdir


def menu():
    global ventas, clientes, catalogo

    opciones = [
        "Cargar un listado de clientes.",
        "Cargar un catálogo de productos.",
        "Registrar ventas realizadas.",
        "Mostrar el listado completo de clientes y productos.",
        "Buscar clientes por provincia.",
        "Mostrar el detalle de ventas con subtotales y total por factura.",
        "Calcular y mostrar el total facturado por cliente.",
        "Mostrar los productos más vendidos.",
        "Generar un resumen de facturación por provincia.",
        "Listar productos sin ventas.",
        "Eliminar productos sin ventas",
        "Eliminar clientes sin ventas\n",
        "Guardar",
        "Salir"
    ]
    print("Elija una opción.")
    for i, opcion in enumerate(opciones, start=1):
        print(f'{i}: {opcion}')
    elegido = input('> ')
    match int(elegido):
        case 1:
            clientes = ingresar_cliente()
        case 2:
            catalogo = cargar_catalogo()

    match int(elegido):
        case 3:
            ventas = ingresar_ventas(clientes, catalogo)

    match int(elegido):
        case 4:
            mostrar_listado(clientes, catalogo)
        case 5:
            clientes_por_provincia(clientes)
        case 6:
            mostrar_detalle_ventas(ventas, catalogo)
        case 7:
            total_facturado(ventas, catalogo)
        case 8:
            productos_mas_vendidos(ventas, catalogo)
        case 9:
            facturacion_por_provincia(ventas, catalogo, clientes)
        case 10:
            productos_sin_ventas(ventas, catalogo)
        case 11:
            catalogo = eliminar_productos(catalogo, clientes)
        case 12:
            clientes = eliminar_clientes(clientes, ventas)
        case 13:
            filepath = path.join(getcwd(), 'guardar')

            file_ventas = path.join(filepath, 'ventas.json')
            file_catalogo = path.join(filepath, 'catalogo.json')
            file_clientes = path.join(filepath, 'clientes.json')

            if ventas is not None:
                guardar_json(file_ventas, ventas)
            if catalogo is not None:
                guardar_json(file_catalogo, catalogo)
            if clientes is not None:
                guardar_json(file_clientes, clientes)

        case 14:
            return False
    return True


if __name__ == "__main__":
    ruta = path.join(getcwd(), 'guardar')
    if not path.exists(ruta):
        mkdir(ruta)
    continuar = True
    ventas = {}
    catalogo = []
    clientes = []
    for name in ['catalogo', 'clientes', 'ventas']:
        subruta = path.join(ruta, name + '.json')
        if path.exists(subruta):
            if name == "catalogo":
                catalogo = abrir_json(subruta)
            elif name == 'clientes':
                clientes = abrir_json(subruta)
            elif name == 'ventas':
                ventas = abrir_json(subruta)
    while continuar:
        continuar = menu()
