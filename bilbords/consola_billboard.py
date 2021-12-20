#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Billboard.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos


"""

import billboard as bb


def ejecutar_cargar_canciones() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    las canciones y las carga.
    Retorno: list
        La lista de canciones con la información del archivo.
    """
    canciones = None
    archivo = input(
        "Por favor ingrese el nombre del archivo CSV con las canciones: ")
    canciones = bb.cargar_canciones(archivo)
    if len(canciones) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking")
    else:
        print("Se cargaron", len(canciones), "canciones a partir del archivo.")
    return canciones


def ejecutar_buscar_cancion(canciones: list) -> None:
    """ Ejecuta la opción de buscar una canción dado el nombre y el año del 
    ranking al cual pertenece 
    """
    cancion = input(
        "Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = int(input("Por favor ingrese el año de la canción que desea buscar: "))

    cancion = bb.buscar_cancion(canciones, cancion, anio)
    if cancion is None:
        print("No se encontró la canción")
    else:
        print("Se encontró la siguiente canción")
        print('Occupa la posición: ' + str(cancion['posicion']))
        print('Nombre de la canción: ' + cancion['nombre_cancion'])
        print('Artista: ' + cancion['nombre_artista'])
        print('Año de publicación: ' + str(cancion['anio']))
        print('Letra: ' + cancion['letra'])


def ejecutar_canciones_anio(canciones: list) -> None:
    """ Ejecuta la opción de consultar las canciones de un año dado 
    """
    anio = int(input("Por favor ingrese el año que desea consultar: "))

    lista = bb.buscar_canciones_anio(canciones, anio)
    index = 1
    for cancion in lista:
        if cancion is None:
            print("No se encontraron canciones")
        else:
            print("Cancion número {} encontrada".format(index))
            print('Occupa la posición: ' + str(cancion['posicion']))
            print('Nombre de la canción: ' + cancion['nombre_cancion'])
            print('Artista: ' + cancion['nombre_artista'])
            print('Año de publicación: ' + str(cancion['anio']))
            index += 1


def ejecutar_canciones_artista_periodo(canciones: list) -> None:
    """ Ejecuta la opción de consultar las canciones de un artista dado en 
    un periodo de tiempo definido 
    """
    artista = input(
        "Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inic = int(
        input("Por favor ingrese el año inicial que desea buscar: "))
    anio_fin = int(input("Por favor ingrese el año final que desea buscar: "))
    index = 1
    lista = bb.buscar_canciones_artista_anio(
        canciones, artista, anio_inic, anio_fin)
    for cancion in lista:
        if cancion is None:
            print("No se encontraron canciones de {} durante ese periodo".format(artista))
        else:
            print("Cancion número {} encontrada durante los años {} y {}".format(
                index, anio_inic, anio_fin))
            print('Occupa la posición: ' + str(cancion['posicion']))
            print('Nombre de la canción: ' + cancion['nombre_cancion'])
            print('Artista: ' + cancion['nombre_artista'])
            print('Año de publicación: ' + str(cancion['anio']))
            index += 1


def ejecutar_todas_canciones_artista(canciones: list) -> None:
    """ Ejecuta la opción de consultar todas las canciones de un artista dado 
    """
    artista = input(
        "Por favor ingrese el nombre del artista que desea buscar: ")

    lista = bb.buscar_canciones_artista(
        canciones, artista)
    print("Estas son todas las canciones de {} en el documento".format(artista))
    print(lista)


def ejecutar_todos_artistas_cancion(canciones: list) -> None:
    """ Ejecuta la opción de consultar todos los artistas que han interpretado 
    una canción dada 
    """
    min = input("Por favor ingrese el nombre de la canción que desea buscar: ")

    lista = bb.buscar_artistas_cancion(canciones, min)
    print("Estos son todos los artistas que han interpretado {} ".format(min))
    print(lista)


def ejecutar_artistas_mas_populares(canciones: list) -> None:
    """ Ejecuta la opción de consultar los artistas más populares 
    """
    min = int(input(
        "Por favor ingrese la cantidad mínima de canciones que desea buscar: "))
    print(bb.artistas_mas_populares(canciones, min))


def ejecutar_artista_estrella(canciones: list) -> None:
    """ Ejecuta la opción de consultar el artista estrella de todos los tiempos 
    """
    print(bb.buscar_artista_estrella(canciones))


def ejecutar_artistas_y_sus_canciones(canciones: list) -> None:
    """ Ejecuta la opción de consultar la lista completa de artistas del Billboard 
    junto con sus canciones 
    """
    print(bb.buscar_artistas_sus_canciones(canciones))


def ejecutar_promedio_canciones_por_artista(canciones: list) -> None:
    """ Ejecuta la opción de consultar la cantidad promedio de canciones que los 
    artistas tienen en el listado de Billboard 
    """
    print(bb.buscar_promedio(canciones))


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            canciones = ejecutar_cargar_canciones()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_cancion(canciones)
        elif opcion_seleccionada == 3:
            ejecutar_canciones_anio(canciones)
        elif opcion_seleccionada == 4:
            ejecutar_canciones_artista_periodo(canciones)
        elif opcion_seleccionada == 5:
            ejecutar_todas_canciones_artista(canciones)
        elif opcion_seleccionada == 6:
            ejecutar_todos_artistas_cancion(canciones)
        elif opcion_seleccionada == 7:
            ejecutar_artistas_mas_populares(canciones)
        elif opcion_seleccionada == 8:
            ejecutar_artista_estrella(canciones)
        elif opcion_seleccionada == 9:
            ejecutar_artistas_y_sus_canciones(canciones)
        elif opcion_seleccionada == 10:
            ejecutar_promedio_canciones_por_artista(canciones)
        elif opcion_seleccionada == 11:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()

