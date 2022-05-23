from gurobipy import GRB, Model
from datos import (meses, horas, dias, comunas, companias,
                   demanda_basica, demanda_critica,
                   compania_abastece_comuna)

'''Definicion de data'''
I = companias
J = comunas
M = meses
N = horas
T = dias

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
x = m.addVars(T, J, M, N, vtype=GRB.INTEGER, name="x_tjmn")
y = m.addVars(I, J, M, vtype=GRB.BINARY, name="y_ijm")
k = m.addVars(I, M, vtype=GRB.INTEGER, name="k_im")
h = m.addVars(I, J, T, M, vtype=GRB.INTEGER, name="h_ijtm")

'''Agregar las variable'''
model.update()

'''Restricciones'''
model.addConstrs()

'''Funcion Objetivo'''
objetivo = []
model.setObjectiva(objetivo, GRB.MAXIMIZE)

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
