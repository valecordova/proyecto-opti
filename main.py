from fileinput import filename
from resultado import create_report
from graficos import graficar
from modelo import resolver_problema

if __name__ == '__main__':
    filename = "reporte_grupo_56.pdf"
    resolver_problema()
    # graficar()
    # create_report(filename)
