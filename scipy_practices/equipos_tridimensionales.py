# %%
from numpy import array
import pandas as pd
df = pd.DataFrame()
df['MODELO'] = ['Bus urbano #27', 'Silla tipo bar', 'Piano',  'Fuente con flores',
                'Bus urbano #27', 'Puesto de Yogurt', 'Playground']
df['USUARIO'] = ['Ted Mosby', 'Art Vandelay', 'Art Vandelay', 'Michael',
                 'Mark Brendanawics', 'Michael', 'Mark Brendanawics', 'LeCorbuiser_2020']
df['PAGO'] = [24.99, 4.99, 4.99, 0, 12, 0, 14, 0]
df['ESTRELLAS'] = [5, 3.5, 3.5, 5, 4, 5, 4.5, 1]
df['COMENTARIO'] = [True, False, False, True, True, True, True, True]
df.info()

# %%


def calcular_estadisticas(descargas:  pd.DataFrame) -> pd.DataFrame:
    index = descargas[descargas['PAGO'] == 0].index
    descargas.drop(index, inplace=True)
    df1 = pd.DataFrame(index=descargas['MODELO'].unique())
    df1['CANTIDAD'] = 0
    df1['PROMEDIO'] = 0
    df1['MAXIMO'] = 0
    df1['MINIMO'] = float('inf')
    df1['ESTRELLAS'] = 0
    df1['DESV. ESTRELLAS'] = 0
    df1['COMENTARIOS'] = 0
    promedio = 0

    for i in range(len(descargas)):
        valor_min = float('inf')
        df1.loc[descargas.iloc[i]['MODELO'], 'CANTIDAD'] += 1

        df1.loc[descargas.iloc[i]['MODELO'],
                'PROMEDIO'] += descargas.iloc[i]['PAGO']

        df1.loc[descargas.iloc[i]['MODELO'], 'MAXIMO'] = max(
            df1.loc[descargas.iloc[i]['MODELO'], 'MAXIMO'], descargas.iloc[i]['PAGO'])

        if descargas.iloc[i]['PAGO'] < df1.loc[descargas.iloc[i]['MODELO'], 'MINIMO']:
            df1.loc[descargas.iloc[i]['MODELO'],
                    'MINIMO'] = descargas.iloc[i]['PAGO']
        df1.loc[descargas.iloc[i]['MODELO'],
                'ESTRELLAS'] += descargas.iloc[i]['ESTRELLAS']

        if descargas.iloc[i]['COMENTARIO']:
            df1.loc[descargas.iloc[i]['MODELO'], 'COMENTARIOS'] += 1

    df1['ESTRELLAS'] = ((df1['ESTRELLAS'] / df1['CANTIDAD'])).round(2)
    df1['PROMEDIO'] = (df1['PROMEDIO'] / df1['CANTIDAD']).round(2)
    df1['DESV. ESTRELLAS'] = (descargas.groupby(
        'MODELO')['ESTRELLAS'].std()).fillna(0).round(2)

    df1.sort_index(inplace=True)
    return df1


# %%
v = calcular_estadisticas(df)

# %%


def calcular_estadisticas(descargas: pd.DataFrame) -> pd.DataFrame:
    filtrado = descargas[descargas["PAGO"] > 0]
    dic = {"CANTIDAD": 0, "PROMEDIO": 0, "MAXIMO": 0, "MINIMO": 0,
           "ESTRELLAS": 0, "DESV. ESTRELLAS": 0, "COMENTARIOS": 0}
    dic["CANTIDAD"] = filtrado["MODELO"].value_counts()
    agrupado = filtrado.groupby("MODELO")
    index = []
    promedio = []
    maximo = []
    minimo = []
    estrellas = []
    desviacion = []
    coment = []
    for name, group in agrupado:
        index.append(name)
        grupo = agrupado.get_group(name)
        promedio.append(grupo["PAGO"].mean())
        maximo.append(grupo["PAGO"].max())
        minimo.append(grupo["PAGO"].min())
        estrellas.append((grupo["ESTRELLAS"].mean()))
        desviacion.append(grupo["ESTRELLAS"].std())
        coment.append(len(grupo[grupo["COMENTARIO"]]))
    dic["PROMEDIO"] = pd.Series(promedio, index=index)
    dic["MAXIMO"] = pd.Series(maximo, index=index)
    dic["MINIMO"] = pd.Series(minimo, index=index)
    dic["ESTRELLAS"] = pd.Series(estrellas, index=index)
    dic["DESV. ESTRELLAS"] = pd.Series(desviacion, index=index)
    dic["COMENTARIOS"] = pd.Series(coment, index=index)
    data = pd.DataFrame(dic)
    data["DESV. ESTRELLAS"] = data["DESV. ESTRELLAS"].round(2).fillna(0)
    data = data.sort_index()

    return data
# %%


def calcular_estadisticas(descargas: pd.DataFrame) -> pd.DataFrame:
    filtrado = descargas[descargas["PAGO"] > 0]
    dic = {"CANTIDAD": 0, "PROMEDIO": 0, "MAXIMO": 0, "MINIMO": 0,
           "ESTRELLAS": 0, "DESV. ESTRELLAS": 0, "COMENTARIOS": 0}
    dic["CANTIDAD"] = filtrado["MODELO"].value_counts()
    agrupado = filtrado.groupby("MODELO")
    index = []
    promedio = []
    maximo = []
    minimo = []
    estrellas = []
    desviacion = []
    coment = []
    for name, group in agrupado:
        index.append(name)
        grupo = agrupado.get_group(name)
        promedio.append(grupo["PAGO"].mean())
        maximo.append(grupo["PAGO"].max())
        minimo.append(grupo["PAGO"].min())
        estrellas.append(grupo["ESTRELLAS"].mean())
        desviacion.append(grupo["ESTRELLAS"].std())
        coment.append(len(grupo[grupo["COMENTARIO"]]))
    dic["PROMEDIO"] = pd.Series(promedio, index=index)
    dic["MAXIMO"] = pd.Series(maximo, index=index)
    dic["MINIMO"] = pd.Series(minimo, index=index)
    dic["ESTRELLAS"] = pd.Series(estrellas, index=index)
    dic["DESV. ESTRELLAS"] = pd.Series(desviacion, index=index)
    dic["COMENTARIOS"] = pd.Series(coment, index=index)
    data = pd.DataFrame(dic)
    data["PROMEDIO"] = data["PROMEDIO"].round(2)
    data["DESV. ESTRELLAS"] = data["DESV. ESTRELLAS"].fillna(0).round(2)
    data = data.sort_index()
    return data


# %%
def calcular_estadisticas(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["PAGO"] > 0]
    df["COMENTARIO"] = df["COMENTARIO"].apply(
        lambda x: int(x))  # 1 if str(x)=="True" else 0
    # agrupamos los datos
    grupo = df.groupby("MODELO")

    # obtenemos los datos
    # contabilizacion de comentariso True
    count_comentarios = grupo["COMENTARIO"].sum().to_list()
    cantidad = grupo["COMENTARIO"].count().to_list()  # cantidad
    # promedio de Pago y estrellas, no se convierte a lista
    prom = grupo[["PAGO", "ESTRELLAS"]].mean()
    min, max = grupo["PAGO"].min().to_list(
    ), grupo["PAGO"].max().to_list()  # minimos y maximos
    desv = grupo["ESTRELLAS"].std().to_list()  # desviacion estandar
    # obtenemos los indices y los metemos en una lista
    indexs = [ind for ind in prom.index]
    # creamos el diccionario donde la llave es el nombre de la columna y el valor es la lista
    new_data = {"CANTIDAD": cantidad, "PROMEDIO": prom.loc[:, ("PAGO")], "MAXIMO": max,
                "MINIMO": min, "ESTRELLAS": prom.loc[:, ("ESTRELLAS")], "DESV. ESTRELLAS": desv}
    new_df = pd.DataFrame(new_data, index=indexs)  # creamos el nuevo DF
    new_df["CANTIDAD"] = new_df["CANTIDAD"].apply(
        lambda x: int(x))  # 1 if str(x)=="True" else 0
    # agregamos la columna pago a partir del anterior df
    new_df["PROMEDIO"] = prom["PAGO"].round(2)
    # agregamos la columna pago a partir del anterior df
    new_df["MAXIMO"] = max
    # agregamos la columna pago a partir del anterior df
    new_df["MINIMO"] = min
    # agregamos la columna estrellas a partir del anterior df
    new_df["ESTRELLAS"] = prom["ESTRELLAS"].round(2)
    new_df["DESV. ESTRELLAS"] = new_df["DESV. ESTRELLAS"].round(
        2).fillna(0)  # redondeamos y rellenamos con 0
    # agregamos la columna comentarios a partir del anterior df
    new_df["COMENTARIOS"] = count_comentarios

    new_df = new_df.sort_index()  # ordenamos el df

    return new_df

# %%


def calcular_estadisticas(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["PAGO"] > 0]
    df["COMENTARIO"] = df["COMENTARIO"].apply(
        lambda x: int(x))  # 1 if str(x)=="True" else 0
    # agrupamos los datos
    grupo = df.groupby("MODELO")

    # obtenemos los datos
    # contabilizacion de comentariso True
    count_comentarios = grupo["COMENTARIO"].sum()
    cantidad = grupo["COMENTARIO"].count()  # cantidad
    # promedio de Pago y estrellas, no se convierte a lista
    prom = grupo[["PAGO", "ESTRELLAS"]].mean()
    min, max = grupo["PAGO"].min(), grupo["PAGO"].max()  # minimos y maximos
    desv = grupo["ESTRELLAS"].std()  # desviacion estandar
    # obtenemos los indices y los metemos en una lista
    indexs = [ind for ind in prom.index]
    # creamos el diccionario donde la llave es el nombre de la columna y el valor es la lista
    new_data = {"CANTIDAD": cantidad, "PROMEDIO": prom.loc[:, ("PAGO")], "MAXIMO": max,
                "MINIMO": min, "ESTRELLAS": prom.loc[:, ("ESTRELLAS")], "DESV. ESTRELLAS": desv}
    new_df = pd.DataFrame(new_data, index=indexs)  # creamos el nuevo DF
    new_df["CANTIDAD"] = new_df["CANTIDAD"].apply(
        lambda x: int(x))  # 1 if str(x)=="True" else 0
    # agregamos la columna pago a partir del anterior df
    new_df["PROMEDIO"] = prom["PAGO"].round(2)
    # agregamos la columna pago a partir del anterior df
    new_df["MAXIMO"] = max
    # agregamos la columna pago a partir del anterior df
    new_df["MINIMO"] = min
    # agregamos la columna estrellas a partir del anterior df
    new_df["ESTRELLAS"] = prom["ESTRELLAS"].round(2)
    new_df["DESV. ESTRELLAS"] = new_df["DESV. ESTRELLAS"].round(
        2).fillna(0)  # redondeamos y rellenamos con 0
    # agregamos la columna comentarios a partir del anterior df
    new_df["COMENTARIOS"] = count_comentarios

    new_df = new_df.sort_index()  # ordenamos el df

    return new_df
# %%
