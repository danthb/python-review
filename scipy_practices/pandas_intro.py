#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import random


def subir_notas(notas: pd.Series) -> pd.Series:
    if notas.mean() > 2.5:
        notas = notas + round(notas.std(), 2)

    for i in range(notas.size):
        nota_actual = notas.iloc[i]
        if nota_actual > 5:
            notas.iloc[i] = 5.0
    return notas


notas = []
for i in range(15):
    nota_generada = random.normalvariate(3.25, 0.98)
    nota_generada = round(nota_generada, 2)
    valida = False
    while not valida:
        if nota_generada >= 1.5 and nota_generada <= 5.0:
            valida = True
        else:
            nota_generada = random.normalvariate(3.25, 0.98)
            nota_generada = round(nota_generada, 2)
    notas.append(nota_generada)
serie_notas = pd.Series(notas)

print(serie_notas)
print("-"*15)
print(subir_notas(serie_notas))
