from gurobipy import GRB, Model, quicksum
from sympy import sqrt
from datos_caudal import agua_compania
from datos import (meses, horas, dias, comunas, companias,
                   demanda_basica, demanda_critica,
                   compania_abastece_comuna, meses_sin_uno)

'''Definicion de data'''
I = companias
J = comunas
M = meses
N = horas
T = dias
N_1 = meses_sin_uno
MG = 10 ** 10
M_ = 13

'''Definir valores de parametros'''
# Este es un diccionario al que se accede con la llave (comuna, compania, dia)
db = demanda_basica
# Este es un diccionario al que se accede con la llave (comuna, compania, dia)
dc = demanda_critica
# Este es un diccionario al que se accede con la llave (comuna, compania)
f = compania_abastece_comuna
# Este es un diccionario al que se accede con la llave (compania)
c = agua_compania

'''Creacion de modelo vacio'''
model = Model()

'''Creacion de variables de decision'''
x = model.addVars(J, I, T, M, N, vtype=GRB.BINARY, name="x_tjmn")
y = model.addVars(J, I, M, vtype=GRB.BINARY, name="y_ijm")
k = model.addVars(I, M, vtype=GRB.INTEGER, name="k_im")
h = model.addVars(J, I, T, M, N, vtype=GRB.INTEGER, name="h_ijtm")

'''Agregar las variable'''
model.update()

'''Restricciones'''

model.addConstrs((x[j, i, t, 1, n] <=
                 ((quicksum(dc[j, i, t, 1, n] for j in J for t in T)
                   )/(c[i, 1])) for j in J for i in I for t in T for n in N), name="r1")

model.addConstrs((x[j, i, t, m, n] <=
                  ((quicksum(dc[j, i, t, m, n] for j in J for t in T)
                    )/(c[i, m])) for j in J for i in I for t in T for m in range(2, M_ + 1)
                  for n in N), name="r2")

model.addConstrs((quicksum(x[j, i, t, m, n]
                 for n in N) <= 4 for j in J for i in I for t in T for m in M),
                 name="r3")

model.addConstrs((x[j, i, t, m, n] + x[j, i, t, m, n + 1] <=
                 1 for j in J for i in I for t in T for m in M for n in N_1),
                 name="r4")

model.addConstrs((h[j, i, t, m, n] <= (1 - x[j, i, t, m, n])*MG
                  for j in J for i in I for t in T for m in M for n in N),
                 name="r5")


model.addConstrs((y[j, i, m] <= (1 + ((db[j, i, t, m] - c[i, m]) /
                                      (db[j, i, t, m] - c[i, m])))
                  for j in J for i in I for t in T for m in M), name="r6")

model.addConstrs((y[j, i, m] >= (db[j, i, t, m] - c[i, m]) /
                  (sqrt((db[j, i, t, m]) ** 2+(c[i, m]) ** 2))
                  for j in J for i in I for t in T for m in M), name="r7")

model.addConstrs((quicksum(h[j, i, t, m, n] for n in N) >= (
    db[j, i, t, m]*(1 - y[j, i, m]))
    for j in J for i in I for t in T for m in M), name="r8")

model.addConstrs((quicksum(h[j, i, t, m, n] for n in N) >= (
    dc[j, i, t, m, n]*y[j, i, m]) for j in J for i in I
    for t in T for m in M), name="r9")

model.addConstrs((quicksum(h[j, i, t, 1, n] for n in N for t in T for j in J)
                  <= (c[i, 1]) for i in I), name="r10")

model.addConstrs((quicksum(h[j, i, t, m, n] for n in N for t in T for j in J)
                  <= (c[i, m] + k[i, m - 1]) for i in I for m in range(2, M_ + 1)), name="r11")

model.addConstrs((k[i, m] == k[i, m - 1] + c[i, m] -
                  quicksum(h[j, i, t, m, n]
                           for n in N for t in T for j in J)
                  for i in I for m in range(2, M_ + 1)), name="r12")

'''Funcion Objetivo'''
objetivo = quicksum(h[j, i, t, m, n]
                    for i in I for j in J for t in T for m in M for n in M)
model.setObjective(objetivo, GRB.MINIMIZE)


def resolver_problema():
    '''Optimizacion del problema'''
    model.optimize()
    '''Imprimir holguras del problema'''
    '''for constr in model.getConstrs():
        print(constr, constr.getAttr("slack"))'''

    '''Restricciones Activas'''
    '''print("\n"+"-"*9+" Restricciones Activas "+"-"*9)
    for constr in model.getConstrs():
        if constr.getAttr("slack") == 0:
            print(f"La restriccion {constr} está activa")'''
