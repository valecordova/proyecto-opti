from fpdf import FPDF


def create_title(pdf):
    pdf.set_font('Arial', 'B', 24)
    pdf.write(5, f"Reporte Grupo 56")
    pdf.ln(10)


def create_subtitle(pdf, section):
    pdf.set_font('Arial', 'B', 18)
    pdf.write(5, f"{section}")
    pdf.ln(10)


def create_report(filename):
    pdf = FPDF(format='Letter')

    '''Titulo'''
    pdf.add_page()
    create_title(pdf)

    '''Seccion 1 Manejo de Soluciones'''
    pdf.add_page()
    section1 = "1. Manejo de Soluciones"
    create_subtitle(pdf, section1)
    # Incluir graficos

    '''Seccion 2 Restricciones Activas'''
    pdf.add_page()
    section2 = "2. Restricciones Activas"
    create_subtitle(pdf, section2)

    pdf.output(filename, 'F')
