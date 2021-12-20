# %%
# Importar y guardar los datos
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
datos = pd.read_csv('exoplanetas.csv')
datos.info()
# %%
# Identificar los campos del dataSet
datos.describe()

# %%
# Función histograma sobre la frecuencia de descubrimientos
valores_histograma = datos[['DESCUBRIMIENTO']]
histogram = valores_histograma.plot.hist(bins=30)
plt.show()
# %%
# Boxplot sobre el DESCUBRIMIENTO y ESTADO_PUBLICACIÓN
datos[['ESTADO_PUBLICACION']].describe()
datos['ESTADO_PUBLICACION'].unique()
datos['DESCUBRIMIENTO'].unique()

# %%
fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax = sns.boxplot(x="ESTADO_PUBLICACION", y="DESCUBRIMIENTO", data=datos)
plt.setp(ax.get_xticklabels(), rotation=90)
# %%
# %%
fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax = sns.boxplot(x="TIPO_DETECCION", y="DESCUBRIMIENTO", data=datos)
plt.setp(ax.get_xticklabels(), rotation=90)

# %%
datos.boxplot(by='TIPO_DETECCION',
              column='DESCUBRIMIENTO')

# %%
# Cocatenacion
plt.rcParams["figure.figsize"] = (20, 5)
# Create a pieplot
df = pd.DataFrame(datos['TIPO_DETECCION'], datos['DESCUBRIMIENTO'])
df1 = pd.concat([datos['TIPO_DETECCION'], datos['DESCUBRIMIENTO']])


# %%
df = pd.DataFrame(index=datos['DESCUBRIMIENTO'].unique(
), columns=datos['TIPO_DETECCION'].unique())
""" df.info() """

dato = datos.groupby(['DESCUBRIMIENTO', 'TIPO_DETECCION'])
for anho, tipo in dato.groups.keys():
    df.loc[anho, tipo] = len(dato.get_group((anho, tipo)))

df = df.fillna(0).sort_index(axis=1)
fig, ax = plt.subplots(figsize=(20, 5))
ax.set_title('Descubrimientos por tipo de detección')
for colum in df:
    ax.plot(df[colum], label=colum)
ax.legend()

plt.show()
df.info()
# %%
