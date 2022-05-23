import pandas as pd

df = pd.read_csv('data.csv', sep=';', header=0,
                 names=['numero', 'comuna', 'provincia', 'poblacion',
                        'compania', 'demanda_critica_comuna',
                        'consumo_actual_persona', 'consumo_actual_mes',
                        'demanda_basica1', 'demanda_basica2'])

meses = list(range(1, 13))

horas = list(range(1, 25))

dias = list(range(1, 31))

comunas = []
[comunas.append(x) for x in df.comuna.tolist() if x not in comunas]

companias = []
[companias.append(x) for x in df.compania.tolist() if x not in companias]

demanda_basica = dict()
for dia in dias:
    dia_n = [dia] * len(df.comuna)
    demanda_en_dia_n = dict(list(
        zip(zip(df.comuna, df.compania, dia_n), df.demanda_basica1)))
    demanda_basica.update(demanda_en_dia_n)

demanda_critica = dict()
for dia in dias:
    dia_n = [dia] * len(df.comuna)
    demanda_en_dia_n = dict(list(
        zip(zip(df.comuna, df.compania, dia_n), df.demanda_critica_comuna)))
    demanda_critica.update(demanda_en_dia_n)

compania_comuna = list(zip(df.comuna, df.compania))

compania_abastece_comuna = dict()
for compania in companias:
    for comuna in comunas:
        if (comuna, compania) in compania_comuna:
            compania_abastece_comuna[(comuna, compania)] = 1
        else:
            compania_abastece_comuna[(comuna, compania)] = 0
