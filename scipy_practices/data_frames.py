#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %%
import pandas as pd
import math

peajes = pd.read_csv('./resources/Peajes.csv', ';')

# %%
# Descriptivas
categoricas = peajes[['NOMBRE', 'CONCESION', 'GEN', 'SENTIDO',
                      'COD_VIA', 'DEP', 'CONCESIONA',
                      'INIC_OPER', 'ETIQUETA']]

# %%
numericas = peajes[['CAT1', 'CAT2', 'CAT3', 'CAT4', 'CAT5',
                    'CAT6', 'CAT7']]
# %%
categoricas.info()
# %%
numericas.info()

# %%
categoricas.describe()
numericas.describe()

# %%
categoricas['DEP'].unique()

# %%
categoricas['COD_VIA'].unique()
# %%
categoricas['DEP'].value_counts()

# %%
categoricas['SENTIDO'].unique()

# %%
numericas.max()

# %%
numericas.idxmax()
# %%
categoricas[['NOMBRE', 'CONCESION', 'DEP']].loc[82]
# %%
# Selección y filtros
ordenados = categoricas.sort_values('CONCESION')
print(ordenados)
# %%
ordenados.iloc[5]
# %%
# Filtros
cundinamarca_tolima = peajes[(peajes['DEP'] == 'Cundinamarca') | (
    peajes['DEP'] == 'Tolima')]
cundinamarca_tolima[['NOMBRE', 'DEP']]
# %%
peajes_cat6y7_costosa = peajes[(
    peajes['CAT6'] > 50000) & (peajes['CAT7'] > 50000)]
peajes_cat6y7_costosa[['NOMBRE', 'CAT6', 'CAT7']]

# %%
valle_atlantico = peajes[peajes['DEP'].isin(['Atlántico', 'Valle del Cauca'])]
valle_atlantico[['NOMBRE', 'DEP']]
# %%


def calcular_distancia_tierra(t1: float, g1: float, t2: float, g2: float) -> float:
    t1_rad = math.radians(t1)
    g1_rad = math.radians(g1)
    t2_rad = math.radians(t2)
    g2_rad = math.radians(g2)
    dist = 6371.01 * math.acos(math.sin(t1_rad) * math.sin(t2_rad) +
                               math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad))
    return round(dist, 2)


def calcular_peaje_cercano(peajes: pd.DataFrame) -> None:
    distancias = []
    cercanos = []
    for i in range(peajes.shape[0]):
        actual = peajes.iloc[i]
        min_distancia = float('inf')
        mas_cerca = ''
        for j in range(peajes.shape[0]):
            if i != j:
                otro = peajes.iloc[j]
                dist = calcular_distancia_tierra(actual['latitud'],
                                                 actual['longitud'],
                                                 otro['latitud'],
                                                 otro['longitud'])
                if dist < min_distancia:
                    min_distancia = dist
                    mas_cerca = otro['NOMBRE']

        distancias.append(min_distancia)
        cercanos.append(mas_cerca)
    print(len(cercanos))
    peajes['MAS CERCANO'] = cercanos
    peajes['DIST_MAS_CERCA'] = distancias


# %%
calcular_peaje_cercano(peajes)

# %%
# Null Data
