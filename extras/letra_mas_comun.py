def letra_mas_comun(cadena):
    cadena = cadena.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("¿", "").replace("¡", "").replace(";", "").replace(":", "").replace("-", "").replace("_", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("/", "").replace("\\", "").replace("*", "").replace("+", "").replace("=", "").replace("<", "").replace(">", "").replace("|", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("&", "").replace("^", "").replace("~", "").replace("`", "").replace("¬", "").replace("'", "").replace("\"", "").replace("°", "").replace("¦", "").replace("·", "").replace(
        "¿", "").replace("¡", "").replace("º", "").replace("ª", "").replace("¬", "").replace("µ", "").replace("·", "").replace("¸", "").replace("¹", "").replace("º", "").replace("¼", "").replace("½", "").replace("¾", "").replace("¿", "").replace("À", "").replace("Á", "").replace("Â", "").replace("Ã", "").replace("Ä", "").replace("Å", "").replace("Æ", "").replace("Ç", "").replace("È", "").replace("É", "").replace("Ê", "").replace("Ë", "").replace("Ì", "").replace("Í", "").replace("Î", "").replace("Ï", "").replace("Ð", "").replace("Ñ", "").replace("Ò", "").replace("Ó", "").replace("Ô", "").replace("Õ", "").replace("Ö", "").replace("Ø", "").replace("Ù", "").replace("Ú", "").replace("Û", "")
    dic = {}
    # llenamos un diccionario con las letras y sus apariciones
    for letra in cadena:
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1
    # obtenemos el valor mayor del diccionario
    mayor = dic[max(dic, key=dic.get)]
    # creamos una lista con tuplas de todas las letras iguales al valor mayor
    lista = [(k, v) for k, v in dic.items() if v == mayor]
    # devolvemos el primer elemento de la última tupla
    letra = sorted(lista)[-1][0]
    return letra


print(letra_mas_comun('A..   A'))

print(letra_mas_comun("piripitiflautica"))

print(letra_mas_comun("ABCDEFGH"))
