def funcion_1() ->str:
    return 'Hola'
def funcion_2(palabra:str)->str:
    return funcion_1()+ str(palabra)

resultado = funcion_2("Juan")

print("El resultado:" + resultado)


import math

def vel_en_caida_libre(altura: float)-> float:
    a = 9.8
    return math.sqrt(2*a*altura)
vel_en_caida_libre(4.5)


def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio:int, dia_actual: int, mes_actual: int, anio_actual: int)->str:
    anio = anio_actual - anio_nacio
    mes = mes_actual - mes_nacio
    if (dia_actual < dia_nacio):
        dia_actual = dia_actual + 30
        mes = mes + 1
        anio = anio -1
    if (mes_actual < mes_nacio):
        mes_actual = mes_actual + 12
        anio = anio - 1
        
    dia = dia_actual - dia_nacio
    return '{},{},{}'.format(anio,mes,dia)

calcular_edad(20,1,1986,16,10,1987)