""" valor_genero y valor_actividad son datos tipos float y especificados en cada caso en los archivos para monstar mensajes en consola """
""" Calculate Adult BMI. peso/weight in (Kg), altura/height in (m) """
def calcular_IMC(peso, altura):
    return round(peso/(altura)**2, 2)

""" Calculate %GC. peso/weight in (Kg), altura/height in (m), edad/age in (años/years) """
def calcular_porcentaje_grasa(peso, altura, edad,valor_genero):
    IMC = calcular_IMC(peso, altura)
    return round((1.2 * IMC) + (0.23 * edad) - 5.4 - valor_genero,2) 

""" Calculate TMB. peso/weight in (Kg), altura/height in (cm), edad/age in (años/years) """
def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    return round((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero,2)


""" Calculate TMBaactivity. peso/weight in (Kg), altura/height in (cm), edad/age in (años/years) """
def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return round(TMB * valor_actividad,2)

""" Calculate cal values to loss weight. peso/weight in (Kg), altura/height in (cm), edad/age in (años/years) """
def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    min_menos = round(TMB - TMB * 0.15, 2)
    max_menos = round(TMB - TMB * 0.20, 2)
    return 'Para adelgazar es recomendado que consumas entre: {} y {} calorías al día.'.format(max_menos, min_menos) 