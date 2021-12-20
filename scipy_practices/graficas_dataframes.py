#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %%
# Load data
import pandas as pd
import matplotlib.pyplot as plt

peajes = pd.read_csv('./resources/Peajes.csv', ';')

# %%
# Data Cleaning
peajes['COD_VIA'] = peajes['COD_VIA'].fillna('Sín código')
peajes['CAT4'] = peajes['CAT4'].fillna(0)
peajes['CAT5'] = peajes['CAT5'].fillna(0)

peajes['INIC_OPER'] = peajes['INIC_OPER'].fillna('01/01/2019')
peajes['FECHA_INICIO_OP'] = pd.to_datetime(
    peajes['INIC_OPER'], infer_datetime_format=True, errors='coerce')

peajes['DEP'] = peajes['DEP'].replace(to_replace='<Null>',
                                      value='Otros')
peajes['DEP'] = peajes['DEP'].replace(to_replace='ANTIOQUIA',
                                      value='Antioquia')

# %%
# Visualization Data
# Boxplot
grafica = peajes[["DEP", "CAT1"]].boxplot(by='DEP', rot=90,
                                          figsize=(10, 6))
plt.title('Tarifas Categoria por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Tarifa en pesos')
plt.show()

# %%
# Multiple Boxplot
grafica1 = peajes[["DEP", "CAT1", "CAT2",
                  "CAT3", "CAT4", "CAT5",
                   "CAT6", "CAT7"]].boxplot(by='DEP', rot=90,
                                            figsize=(10, 6))

k = 1
for element in grafica1:
    for i in element:
        i.set_title('Categoria'+str(k))
        i.set_xlabel('Departamento')
        i.set_ylabel('Tarifa en pesos')
        k += 1
plt.show()

# %%
# Multiplots
primera = peajes[peajes['DEP'] == 'Cundinamarca'].plot(kind='scatter',
                                                       x='CAT1', y='CAT2',
                                                       color='DarkBlue', label='1 a 2',
                                                       figsize=(10, 6))

segunda = peajes[peajes['DEP'] == 'Cundinamarca'].plot(kind='scatter',
                                                       x='CAT1', y='CAT3',
                                                       color='DarkGreen', label='1 a 2',
                                                       ax=primera, figsize=(10, 6))

tercera = peajes[peajes['DEP'] == 'Cundinamarca'].plot(kind='scatter',
                                                       x='CAT1', y='CAT4',
                                                       color='DarkRed', label='1 a 2',
                                                       ax=segunda, figsize=(10, 6))
plt.show()

# %%
# Multiplots
cuarta = peajes[peajes['DEP'] == 'Cundinamarca'].plot(kind='scatter',
                                                      x='CAT1', y='CAT2', c='CAT3',
                                                      s=50, figsize=(10, 6))
plt.show()

# %%
# Multiplots
quinta = peajes[peajes['DEP'] == 'Cundinamarca'].plot(kind='scatter',
                                                      x='CAT1', y='CAT2',
                                                      c='CAT3', s='CAT4',
                                                      figsize=(10, 6))
plt.show()
# %%
# Checking
peajes.info()
fechas_nulas = peajes[peajes['INIC_OPER'].isna()]
fechas_nulas[['NOMBRE', 'INIC_OPER', 'GEN']]
peajes['FECHA_INICIO_OP'].head()
(peajes['DEP']).unique()


# %%
