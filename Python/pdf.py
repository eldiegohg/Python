import PyPDF2

def leer_pdf(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo:
        lector_pdf = PyPDF2.PdfFileReader(archivo)
        num_paginas = lector_pdf.numPages

        for pagina_numero in range(num_paginas):
            pagina = lector_pdf.getPage(pagina_numero)
            texto = pagina.extractText()
            print(f"Contenido de la página {pagina_numero + 1}:\n{texto}\n")

# Ruta del archivo PDF que deseas leer
ruta_del_archivo_pdf = r'C:\Users\DIEGO\Documents\Python\TSP scripts Diego Hdz.pdf'

# Llama a la función para leer el archivo PDF
leer_pdf(ruta_del_archivo_pdf)
