from docx import Document

def abrir_archivo_word(ruta_archivo):
    # Abre el archivo de Word
    doc = Document(ruta_archivo)

    # Itera sobre los párrafos del documento
    for paragraph in doc.paragraphs:
        print(paragraph.text)

# Ruta del archivo de Word que deseas abrir
ruta_del_archivo = r'C:\Users\DIEGO\Documents\Python\21393091_Hernández_García-Maquetación de los mapas SM63.docx'

# Llama a la función para abrir el archivo de Word
abrir_archivo_word(ruta_del_archivo)
