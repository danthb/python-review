# Calcular costo de las boletas del cine
tipos_sala = {"Dinamix": 18800, "3D": 15500, "2D": 11300}


def calcular_tarifa_basica(cantidad_boletas: int, tipo_sala: str) -> int:
    tarifa_basica = 0
    tarifa_basica = tipos_sala[tipo_sala] * cantidad_boletas
    return tarifa_basica


def calcular_costo_boletas(cantidad_boletas: int, tipo_sala: str, hora_pico: bool, pago_tarjeta_cinema: bool, reserva: bool) -> int:
    """
    Calcula el costo de las boletas del cine
    :param cantidad_boletas: int
    :param tipo_sala: str
    :param hora_pico: bool
    :param pago_tarjeta_cinema: bool
    :param reserva: bool
    :return: int
    """

    descuento = 0
    recargo = 0
    tarifa_basica = calcular_tarifa_basica(cantidad_boletas, tipo_sala)
    if hora_pico:
        if tipo_sala == "Dinamix":
            descuento = tarifa_basica * 0.50
        elif tipo_sala == "3D" or tipo_sala == "2D":
            descuento = tarifa_basica * 0.25
    elif not hora_pico:
        descuento += tarifa_basica * 0.10
        if cantidad_boletas >= 3:
            descuento += cantidad_boletas * 500

    if reserva:
        recargo = 20000
    elif not reserva:
        recargo = 0
    else:
        print("Error en la reserva")

    if pago_tarjeta_cinema:
        descuento += tarifa_basica * 0.05

    return int(tarifa_basica - descuento + recargo)


print(calcular_costo_boletas(3, "Dinamix", True, True, True))
print(calcular_costo_boletas(3, "Dinamix", True, True, False))
print(calcular_costo_boletas(3, "Dinamix", True, False, True))
print(calcular_costo_boletas(3, "Dinamix", True, False, False))
print(calcular_costo_boletas(3, "Dinamix", False, True, True))
