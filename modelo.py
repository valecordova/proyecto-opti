from gurobipy import GRB, Model, quicksum
from datos import (meses, horas, dias, comunas, companias,
                   demanda_basica, demanda_critica,
                   compania_abastece_comuna, comuna_compania,
                   meses_sin_uno)

'''Definicion de data'''
I = companias
J = comunas
M = meses
N = horas
T = dias
N_1 = meses_sin_uno
'''Definir valores de parametros'''
# Este es un diccionario al que se accede con la llave (comuna, compania, dia)
db = demanda_basica
# Este es un diccionario al que se accede con la llave (comuna, compania, dia)
dc = demanda_critica
# Este es un diccionario al que se accede con la llave (comuna, compania)
f = compania_abastece_comuna

'''Creacion de modelo vacio'''
model = Model()

'''Creacion de variables de decision'''
x = model.addVars(T, J, M, N, vtype=GRB.BINARY, name="x_tjmn")
y = model.addVars(J, I, M, vtype=GRB.BINARY, name="y_ijm")
k = model.addVars(I, M, vtype=GRB.INTEGER, name="k_im")
h = model.addVars(J, I, T, M, vtype=GRB.INTEGER, name="h_ijtm")

'''Agregar las variable'''
model.update()

'''Restricciones'''
# Cortes de agua
model.addConstrs((quicksum(x[t, j, m, n]
                 for n in N) <= 4 for j in J for t in T for m in M), name="r1")
model.addConstrs((((x[j, t, m, n] + x[j, t, m, (n+1)]) <= 1)
                  for j in J for t in T for m in M for n in N_1), name="r2")
# Demandas y capacidades
model.addConstrs((h[j, i, t, m] >= (db[j, i, t] * (1 - y[j, i, m]))
                 for j, i in comuna_compania for t in T for m in M),
                 name="r3")

model.addConstrs((h[j, i, t, m] >= (dc[j, i, t] * y[j, i, m])
                 for j, i in comuna_compania for t in T for m in M),
                 name="r4")


'''Funcion Objetivo'''
objetivo = quicksum(h[j, i, t, m] for i in I for j in J for t in T for m in M)
model.setObjective(objetivo, GRB.MINIMIZE)

'''Optimizacion del problema'''
model.optimize()

'''Imprimir holguras del problema'''
for constr in model.getConstrs():
    print(constr, constr.getAttr("slack"))

'''Restricciones Activas'''
print("\n"+"-"*9+" Restricciones Activas "+"-"*9)
for constr in model.getConstrs():
    if constr.getAttr("slack") == 0:
        print(f"La restriccion {constr} está activa")
