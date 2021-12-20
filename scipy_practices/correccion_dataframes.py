#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %%
import pandas as pd
import math

peajes = pd.read_csv('./resources/Peajes.csv', ';')

peajes.info()
# %%
peajes['COD_VIA'] = peajes['COD_VIA'].fillna('Sín código')

peajes['CAT4'] = peajes['CAT4'].fillna(0)
peajes['CAT5'] = peajes['CAT5'].fillna(0)

fechas_nulas = peajes[peajes['INIC_OPER'].isna()]

# %%
fechas_nulas[['NOMBRE', 'INIC_OPER', 'GEN']]

# %%
peajes['INIC_OPER'] = peajes['INIC_OPER'].fillna('01/01/2019')
# %%
peajes.info()
# %%
peajes['FECHA_INICIO_OP'] = pd.to_datetime(
    peajes['INIC_OPER'], infer_datetime_format=True, errors='coerce')
# %%
peajes['FECHA_INICIO_OP'].head()
# %%
