import csv

#Definimos la function createCSV
def function_createCSV():

    # abrir archivo csv en modo escritura
    import row as row
    f = open('./file.csv', 'w')
    # Creamos el csv.writer
    writer = csv.writer(f)

    # Creamos el row de csv
    writer.writerow(row)

    # cerramos el archivo
    f.close()

def function_writeCSV():

    #Creamos las filas y columnas
    header = ['name', 'surname', 'age']
    #Rellenamos las filas y columnas
    data = [
        ['Guillem', 'Jimenez', '30'],
        ['Adrian', 'Berruezo', '34'],
        ['Sebastian', 'Casco', '19'],
    ]
    #data = ['X', 'X', 'X']
    #Escribimos sobre el archivo CSV
    with open('file.csv', 'w', encoding='UTF8') as f:

        writer = csv.writer(f)

        # Escribimos la fila
        writer.writerow(header)

        # Escribimos los datos
        writer.writerow(data)


def function_readerCSV():

    with open('file.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
    for row in reader:
        #Imprimir los resultados
        print(row)

#Llamamos a las funciones
function_createCSV
function_writeCSV
function_readerCSV