import csv

def function_createCSV():
    row_list = [["Name", "Surname", "Age"],
                ["Guillem", "Jimenez", "30"],
                ["Adrian", "Berruezo", "34"],
                ["Sebastian", "Casco", "19"]]
    with open('file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

def function_readCSV():
    with open('file.csv', newline='', encoding='utf-8') as file:
    # Leemos el archivo csv
      csvFile = csv.reader(file)

    # Mostramos los datos del archivo csv
      for lines in csvFile:
            print(lines)

function_createCSV()
function_readCSV()

