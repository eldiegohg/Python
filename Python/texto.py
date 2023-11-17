# Ruta del archivo de texto
ruta_del_archivo = r'C:\Users\DIEGO\Documents\Python\tarea_buscar.txt'

# Abre el archivo de texto en modo lectura ('r')
with open(ruta_del_archivo, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
