import pandas as pd

df = pd.read_csv('data.csv', sep=';', header=0,
                 names=['numero', 'comuna', 'provincia', 'poblacion',
                        'compania', 'demanda_critica_comuna',
                        'consumo_actual_persona', 'consumo_actual_mes',
                        'demanda_basica'])

meses = list(range(1, 13))

meses_sin_uno = list(range(1, 12))

horas = list(range(1, 25))

dias = list(range(1, 31))

comunas = []
[comunas.append(x) for x in df.comuna.tolist() if x not in comunas]

companias = []
[companias.append(x) for x in df.compania.tolist() if x not in companias]

demanda_basica = dict()
for mes in meses:
    mes_n = [mes] * len(comunas)
    for dia in dias:
        dia_n = [dia] * len(comunas)
        demanda_en_dia_n = dict(list(
            zip(zip(df.comuna, df.compania, dia_n, mes_n),
                df.demanda_basica)))
        demanda_basica.update(demanda_en_dia_n)

demanda_critica = dict()
for mes in meses:
    mes_n = [mes] * len(comunas)
    for dia in dias:
        dia_n = [dia] * len(comunas)
        demanda_en_dia_n = dict(list(
            zip(zip(df.comuna, df.compania, dia_n, mes_n),
                df.demanda_critica_comuna)))
        demanda_critica.update(demanda_en_dia_n)

comuna_compania = list(zip(df.comuna, df.compania))

compania_abastece_comuna = dict()
for compania in companias:
    for comuna in comunas:
        if (comuna, compania) in comuna_compania:
            compania_abastece_comuna[(comuna, compania)] = 1
        else:
            compania_abastece_comuna[(comuna, compania)] = 0

'''
for key in demanda_basica.keys():
    if key[0] == 'Santiago ' or key[0] == 'Santiago':
        print(key)

# '''
