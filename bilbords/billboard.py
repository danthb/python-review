""" 
Cargar canciones desde un archivo csv
"""


def cargar_canciones(filename: str) -> list:
    """
    Inizialize the billboard with the file.
    """
    # next(f)
    # variable to delete the first line of the file
    counter = 0
    billboard = []
    # El numero 1 representa que debe ser un numero entero y debe ser convertido a int()
    tipo_datos = [1, 0, 0, 1, 0]
    # Lista para formar el diccionario de cada cancion
    llaves = ['posicion', 'nombre_cancion', 'nombre_artista', 'anio', 'letra']
    with open(filename, 'r') as f:
        for line in f:
            if counter != 0:
                dict = {}
                index = 0
                individual = line.split(',')
                for element in individual:
                    if tipo_datos[index]:
                        dict[llaves[index]] = int(element)
                    else:
                        dict[llaves[index]] = element
                    index += 1
                billboard.append(dict)
            else:
                counter += 1
    return billboard


def buscar_cancion(billboard: list, nombre_cancion: str, anio: int) -> list:
    resultado = []
    str(anio)
    for cancion in billboard:
        if cancion['nombre_cancion'] == nombre_cancion and cancion['anio'] == anio:
            resultado.append(cancion)
    if resultado:
        return resultado[0]
    else:
        return None


def buscar_canciones_anio(billboard: list, anio: int) -> list:
    resultado = []
    for cancion in billboard:
        if cancion['anio'] == anio:
            resultado.append(cancion)
    if resultado:
        return resultado
    else:
        return None


def buscar_canciones_artista_anio(billboard: list, nombre_artista: str, anio_inic: int, anio_fin: int) -> list:
    resultado = []
    for cancion in billboard:
        if (cancion['nombre_artista'] == nombre_artista and cancion['anio'] >= anio_inic and cancion['anio'] <= anio_fin):
            resultado.append(cancion)
    if resultado:
        return resultado
    else:
        return None


def buscar_canciones_artista(billboard: list, nombre_artista: str) -> list:
    resultado = []
    for cancion in billboard:
        if (cancion['nombre_artista'] == nombre_artista):
            resultado.append(cancion['nombre_cancion'])
    if resultado:
        return resultado
    else:
        return None


def buscar_artistas_cancion(billboard: list, nombre_cancion: str) -> list:
    resultado = []
    for cancion in billboard:
        if (cancion['nombre_cancion'] == nombre_cancion):
            resultado.append(cancion['nombre_artista'])
    if resultado:
        return resultado
    else:
        return None


def artistas_mas_populares(billboard: list, cantidad: int) -> dict:

    contador = {}

    for i in range(0, len(billboard)):
        datos = billboard[i]
        artista = datos.get("nombre_artista")
        contador[artista] = contador.get(artista, 0)+1

    resultado = {artista: contador for (
        artista, contador) in contador.items() if contador > cantidad}

    return resultado


def buscar_artista_estrella(billboard: list) -> dict:

    contador = {}
    mayor = 0

    for i in range(0, len(billboard)):
        datos = billboard[i]
        artista = datos.get("nombre_artista")
        contador[artista] = contador.get(artista, 0)+1
    for element in contador:
        if contador[element] > mayor:
            mayor = contador[element]
            artista_estrella = element
    return {artista_estrella: mayor}


def buscar_artistas_sus_canciones(billboard: list) -> list:
    albumns = {}
    for index, item in enumerate(billboard):
        artista = item.get("nombre_artista")
        albumns[artista] = albumns.get(
            artista, []) + [item.get("nombre_cancion")]
    print(len(albumns.keys()))
    return albumns


def buscar_promedio(billboard: list) -> float:
    contador = []
    cantidad_artistas = len(buscar_artistas_sus_canciones(billboard))
    cantidad_canciones = 0
    for item in billboard:
        artista = item.get("nombre_artista")
        cancion = item.get("nombre_cancion")
        if artista + cancion not in contador:
            contador.append(artista+cancion)
            cantidad_canciones += 1

    return cantidad_canciones/cantidad_artistas
