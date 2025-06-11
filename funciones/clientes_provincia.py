from .util import mostar_tabla_provincias


def clientes_por_provincia(clnt):
    # 5. Buscar clientes por provincia usando un filtro dinámico.
    # - Utilizar una expresión de filtrado con comprensión de listas y mostrar los resultados coincidentes.
    provincias = ["Buenos Aires", "Ciudad Autónoma de Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba",
                  "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones",
                  "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe",
                  "Santiago del Estero", "Tierra del Fuego", "Tucumán"]

    mostar_tabla_provincias(provincias)

    print('Elija la provincia de los clientes a mostrar')
    while True:
        opcion = input('> ')
        mensaje = None
        if opcion.isdigit():
            if 0 <= int(opcion) < len(provincias):
                print(f'{cl['ID']}: {cl['nombre']}' for cl in clnt if cl['provincia'] == provincias[int(opcion)])

            else:  # esto ocurre si la opción ingresada es mayor a 23 o menor a 0.
                mensaje = "la opción ingresada es inválida."
        else:  # esto ocurre si se ingresa otra cosa que no sea un número.
            mensaje = "ingrese un número natural del 0 a 23."

        print(mensaje, ' Intente de nuevo.')