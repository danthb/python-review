def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int) -> str:

    if not anio_actual % 4:
        if not anio_actual % 100:
            if not anio_actual % 400:
                bisiesto = True
            else:
                bisiesto = False
        else:
            bisiesto = True
    else:
        bisiesto = False

    if(dia_actual < dia_nacio and mes_actual < mes_nacio and anio_actual < anio_nacio):
        return 'Aún no nace'
    if(dia_actual < dia_nacio):
        mes_actual = mes_actual - 1
        if(mes_actual == 1 or mes_actual == 3 or mes_actual == 5 or mes_actual == 7 or mes_actual == 8 or mes_actual == 10 or mes_actual == 12):
            dia_actual += 31
        elif(mes_actual == 2 and bisiesto):
            dia_actual += 29
        elif(mes_actual == 2 and bisiesto == False):
            dia_actual += 28
        else:
            dia_actual += 30
    dia = dia_actual - dia_nacio
    if(mes_actual == 0):
        mes_actual = 12
        anio_actual = anio_actual-1
    elif(mes_actual < mes_nacio):
        mes_actual = mes_actual + 12
        anio_actual = anio_actual - 1

    mes = mes_actual - mes_nacio
    anio = anio_actual - anio_nacio
    return '{},{},{}'.format(anio, mes, dia)


print(calcular_edad(25, 10, 1993, 4, 8, 2019))
