import pandas as pd
from datos import meses

df = pd.read_csv('datacaudal.csv', sep=",", header=0,
                 names=['fuente', 'caudal', 'compania'])

companias = []
[companias.append(x) for x in df.compania.tolist() if x not in companias]

agua_compania = dict()
for mes in meses:
    for compania in companias:
        caudal_por_compania = df.loc[df['compania']
                                     == compania, 'caudal'].sum()
        agua_compania[compania, mes] = caudal_por_compania * \
            30 * 24 * 3600

print(agua_compania)
