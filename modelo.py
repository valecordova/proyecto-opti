from gurobipy import GRB, Model

# Definicion de data

# Definir valores de parametros

# Creacion de modelo vacio
model = Model()

# Creacion de variables de decision
manu = model.addVars(vtype=GRB.INTEGER, name="manu")

# Agregar las variable
model.update()

# Restricciones
model.addConstrs()

# Funcion Objetivo
objetivo = []
model.setObjectiva(objetivo, GRB.MAXIMIZE)

# Optimizacion del problema
model.optimize()

# Imprimir holguras del problema
for constr in model.getConstrs():
    print(constr, constr.getAttr("slack"))

# Restricciones Activas
print("\n"+"-"*9+" Restricciones Activas "+"-"*9)
for constr in model.getConstrs():
    if constr.getAttr("slack") == 0:
        print(f"La restriccion {constr} está activa")
