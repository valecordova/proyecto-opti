import pandas as pd

df = pd.read_csv('data.csv', sep=';', header=0,
                 names=['numero', 'comuna', 'provincia', 'poblacion',
                        'compania', 'demanda_critica_comuna',
                        'consumo_actual_persona', 'consumo_actual_mes',
                        'demanda_basica1', 'demanda_basica2'])

dic = list(zip(df.numero, df.comuna))

demanda_basica = dict(list(
    zip(zip(df.comuna, df.compania), df.demanda_basica1)))

demanda_critica = dict(list(
    zip(zip(df.comuna, df.compania), df.demanda_critica_comuna)))

meses = list(range(1, 13))

horas = list(range(1, 25))

dias = list(range(1, 32))

comunas = df.comuna.tolist()

companias = df.compania.tolist()

print(companias)
