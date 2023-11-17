import openpyxl

# Ruta del archivo Excel
ruta_del_archivo = r'C:\Users\DIEGO\Documents\Python\Documento en excel.xlsx'

# Carga el archivo Excel
libro_excel = openpyxl.load_workbook(ruta_del_archivo)

# Selecciona la hoja de trabajo (puedes cambiar el nombre de la hoja según tu archivo)
hoja = libro_excel['NombreDeTuHoja']

# Itera sobre las filas de la hoja
for fila in hoja.iter_rows():
    for celda in fila:
        print(celda.value)

# Cierra el archivo Excel
libro_excel.close()
