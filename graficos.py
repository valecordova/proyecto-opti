from matplotlib import pyplot as plt
from datos import df


def graficar():
    df.plot(x="comuna", y="demanda_basica", kind="bar", figsize=(10, 10))
    plt.savefig('graficos/comuna_demanda_basica.png', bbox_inches="tight")

    df.plot(x="comuna", y="demanda_critica_comuna",
            kind="bar", figsize=(10, 10))
    plt.savefig('graficos/comuna_demanda_critica.png', bbox_inches="tight")

    df.plot(x="comuna", y="poblacion", kind="bar", figsize=(10, 10))
    plt.savefig('graficos/comuna_poblacion.png', bbox_inches="tight")
