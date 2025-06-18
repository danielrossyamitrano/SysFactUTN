from json import dump, load


def guardar_json(filename, datos):
    with open(filename, mode='wt', encoding="utf-8") as file:
        dump(datos, file, indent=2, ensure_ascii=False)

def abrir_json(filepath):
    with open(filepath, mode="rt", encoding='utf-8') as file:
        return load(file)

def mostar_tabla_provincias(provincias):
    for i, provincia in enumerate(provincias, start=1):
        # este bloque preseta las opciones en dos columnas, segun si el índice es par o no.
        text = f'{i - 1}: {provincias[i - 1]}'
        if i % 2 == 0:  # si el índice es par, entonces nos encontramos en la segunda columna. Corresponde un salto.
            fin = '\n'
        elif i in [5, 9, 13, 15, 17]:  # estos son casos especiales que requieren una tabulación mayor.
            fin = '\t' * 4
        elif i == 23:  # Tierra del fuego es la provincia con más caracteres, requiere solo una tabulación.
            fin = '\t'
        else:  # el remanente de los casos solo utilizan 3 tabulaciones.
            fin = '\t' * 3

        print(text, end=fin)  # imprimimos el texto tabulado.