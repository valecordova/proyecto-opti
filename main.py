from fileinput import filename
from resultado import create_report
from graficos import graficar

if __name__ == '__main__':
    filename = "reporte_grupo_56.pdf"
    graficar()
    create_report(filename)
