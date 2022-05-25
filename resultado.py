from fpdf import FPDF


def create_title(pdf):
    pdf.set_font('Arial', 'B', 24)
    pdf.write(5, f"Reporte Grupo 56")
    pdf.ln(10)


def create_subtitle(pdf, section):
    pdf.set_font('Arial', 'B', 18)
    pdf.write(5, f"{section}")
    pdf.ln(10)


def create_subsubtitle(pdf, subsection):
    pdf.set_font('Arial', 'B', 14)
    pdf.write(5, f"{subsection}")
    pdf.ln(10)


def create_names(pdf, subsection):
    pdf.set_font('Arial', 'I', 12)
    pdf.write(5, f"{subsection}")
    pdf.ln(10)


def values(pdf, subsection):
    pdf.set_font('Arial', '', 12)
    pdf.write(5, f"{subsection}")
    pdf.ln(5)


def create_report(filename):
    pdf = FPDF(format='Letter')

    '''Titulo'''
    pdf.add_page()
    create_title(pdf)
    names = 'David Alejandro Boyd Rodríguez sección 2\nMaría Francisca Carrasco Polanco sección 3\nAlicia Valentina Córdova Véliz sección 4\nMaría Clara Pinto Chadwick sección alumno 4\nJoaquín Alejandro Tapia Troncoso sección 4\nNicole Valeria Valenzuela Castillo sección 4'
    create_names(pdf, names)

    '''Seccion 1 Manejo de Soluciones'''
    pdf.add_page()
    section1 = "1. Manejo de Soluciones"
    create_subtitle(pdf, section1)
    '''Seccion 1.1 Valor Objetivo'''
    subsection1 = "1.1 Valor Objetivo"
    create_subsubtitle(pdf, subsection1)
    '''Seccion 1.2 Soluciones'''
    subsection2 = "1.2 Soluciones"
    create_subsubtitle(pdf, subsection2)
    # Incluir graficos

    '''Seccion 2 Restricciones Activas'''
    pdf.add_page()
    section2 = "2. Restricciones Activas"
    create_subtitle(pdf, section2)

    '''Seccion 3 Graficos'''
    pdf.add_page()
    section3 = "3. Gráficos"
    create_subtitle(pdf, section3)
    pdf.image('graficos/comuna_demanda_basica.png', w=150)
    pdf.image('graficos/comuna_demanda_critica.png', w=150)
    pdf.image('graficos/comuna_poblacion.png', w=150)

    pdf.output(filename, 'F')
