from .util import mostar_tabla_provincias


def elegir_provincia():
    """Permite al usuario elegir la pronvincia a la que pertenece.

    Devuelve el string de la provincia elegida.
    """

    provincias = ["Buenos Aires", "Ciudad Autónoma de Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba",
                  "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones",
                  "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe",
                  "Santiago del Estero", "Tierra del Fuego", "Tucumán"]

    mostar_tabla_provincias(provincias)

    print('Elija la pronvicia a la que pertence el cliente')
    while True:
        opcion = input('> ')
        if opcion.isdigit():
            if 0 <= int(opcion) < len(provincias):
                return provincias[int(opcion)]
            else:  # esto ocurre si la opción ingresada es mayor a 23 o menor a 0.
                mensaje = "la opción ingresada es inválida."
        else:  # esto ocurre si se ingresa otra cosa que no sea un número.
            mensaje = "ingrese un número natural del 0 a 23."

        print(mensaje, ' Intente de nuevo.')