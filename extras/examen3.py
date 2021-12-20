def funcion(x: int, n: int) -> int:
    resultado = 1
    i = n * x
    while i >= 0:
        resultado *= i**x
        i -= 1
    return resultado


print(funcion(2, 5))
