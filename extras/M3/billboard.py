# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:15:00 2021

@author: ORLAREZ
"""

def cargar_canciones (ruta_archivo:str)->list:
    """Recibe el nombre de un archivo CSV con los datos de
    las canciones y las carga.
    Retorno: list
        La lista de canciones con la información del archivo.
    """   
    canciones=[]
    archivo = open(ruta_archivo)
    """Lee el encabezado del archivo y lo descarta"""
    archivo.readline()
    """Lee los datos de las canciones de los archivos y crea
    los diccionarios y los cargar en una lista
    """
    linea=archivo.readline()
    while len(linea)>0:
        datos=linea.split(',')
        cancion={}
        cancion["posicion"]=datos[0]
        cancion["nombre_cancion"]=datos[1]
        cancion["nombre_artista"]=datos[2]
        cancion["anio"]=datos[3]
        cancion["letra"]=datos[4]
        canciones.append(cancion)
        linea=archivo.readline()
        
    archivo.close()
    return canciones

def buscar_cancion(canciones:list, cancion:str, anio:int)->dict:
    """Recibe la lista de canciones cargada y ubica la canción de acuerso a 
    los parametros ingresados.
    Retorno: dict
        Diccionarios con los datos de la canción buscada.
    """   
    datos_cancion=None
    control=True
    i=0
    
    while i < len(canciones) and control:
        datos=canciones[i]
        if datos.get("nombre_cancion")==cancion and int(datos.get("anio"))==anio:
            datos_cancion=datos
            control=False
        i+=1
 
    return datos_cancion

def canciones_anio (canciones:list, anio:int)->list:
    """Recibe la lista de canciones cargada y ubica las canciones del año
    ingresado.
    Retorno: list
        Lista con los datos de las canciones del año sin el item letra.
    """  
    canciones_anio=[]   
        
    for i in range (0,len(canciones)):
        datos=canciones[i]
        cancion={}
        if int(datos.get("anio"))==anio:
            cancion=datos.copy()
            cancion.pop("letra")
            canciones_anio.append(cancion)
         
    return canciones_anio

def canciones_artista_periodo (canciones:list, artista:str, anio_inic:int, anio_fin:int)->list:
    """Recibe la lista de canciones cargada y ubica las canciones del acuerdo
    a los parametros ingresados.
    Retorno: list
        Lista con los datos de las canciones del periodo sin el item letra.
    """  
    canciones_artista=[]   
        
    for i in range (0,len(canciones)):
        datos=canciones[i]
        cancion={}
        if datos.get("nombre_artista")==artista and int(datos.get("anio"))>=anio_inic and int(datos.get("anio"))<=anio_fin:
            cancion=datos.copy()
            cancion.pop("letra")
            canciones_artista.append(cancion)
       
    return canciones_artista
 
def todas_canciones_artista (canciones:list, artista:str)->list:
    """Recibe la lista de canciones cargada y ubica las canciones del artista
    ingresado.
    Retorno: list
        Lista con los nombres de las canciones del artista.
    """ 
    canciones_artista=[]   
        
    for i in range (0,len(canciones)):
        datos=canciones[i]
        if datos.get("nombre_artista")==artista:
           canciones_artista.append(datos.get("nombre_cancion"))
       
    return canciones_artista    

def todos_artistas_cancion (canciones:list, cancion:str)->list:
    """Recibe la lista de canciones cargada y ubica las artistas de la canción
    ingresada.
    Retorno: list
        Lista con los nombres de los artistas de la canción.
    """ 
    cancion_artistas=[]   
        
    for i in range (0,len(canciones)):
        datos=canciones[i]
        if datos.get("nombre_cancion")==cancion:
           cancion_artistas.append(datos.get("nombre_artista"))
       
    return cancion_artistas   

def artistas_mas_populares (canciones:list, cantidad:int)->dict:
    """Recibe la lista de canciones cargada y ubica los artistas con mas
    canciones por encima del parametro ingresada.
    Retorno: dict
        Diccionario con los nombres de los artistas y la cantidad de canciones.
    """ 
    contador={}  
        
    for i in range (0,len(canciones)):
        datos=canciones[i]
        artista = datos.get("nombre_artista")
        contador[artista]=contador.get(artista,0)+1
    
    resultado={artista:contador for (artista,contador) in contador.items() if contador > cantidad}
       
    return resultado   

def artista_estrella (canciones:list)->dict:
    """Recibe la lista de canciones cargada y ubica las artistas con mas exitos.
    Retorno: dict
        Dicionarios con el artista y la cantidad de exitos.
    """ 
    contador={}  
        
    for i in range (0,len(canciones)):
        datos=canciones[i]
        artista = datos.get("nombre_artista")
        contador[artista]=contador.get(artista,0)+1
    
    resultado={}
    artista=max(contador, key = contador.get)
    resultado[artista]=contador.get(artista)
       
    return resultado   

def artistas_y_sus_canciones (canciones:list)->dict:
    """Recibe la lista de canciones cargada y ubica todas las canciones por
    artista.
    Retorno: dict
        Dicionarios con los artista y la su lista de canciones.
    """ 
    contador={}  
        
    for i in range (0,len(canciones)):
        datos=canciones[i]
        artista = datos.get("nombre_artista")
        if artista not in contador:
            contador[artista]=list()
        contador[artista].append(datos.get("nombre_cancion"))
    
    
    return contador 

def promedio_canciones_por_artista (canciones:list)->float:
    """Recibe la lista de canciones cargada y calcula el promedio de canciones
    por artista.
    Retorno: float
        Varible con el promedio calculado.
    """
    contador=[]
    cantidad_artistas=len(artistas_y_sus_canciones(canciones))
    cantidad_canciones=0
        
    for i in range (0,len(canciones)):
        datos=canciones[i]
        artista = datos.get("nombre_artista")
        cancion = datos.get("nombre_cancion")
        if artista+cancion not in contador:
            cantidad_canciones+=1
        contador.append(artista+cancion)
    return (cantidad_canciones/cantidad_artistas)
