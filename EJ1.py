import xml.etree.ElementTree as variable
def crearxml ():
#creamios el root 
    r = variable.Element('students')

    child1 = variable.SubElement(r,'student')
    sub1 = variable.SubElement(child1, 'name')
    sub2 = variable.SubElement(child1, 'surname')
    sub3 = variable.SubElement(child1, 'email')
    sub4 = variable.SubElement(child1, 'dni')

    child2 = variable.SubElement(r,'student')
    sub1 = variable.SubElement(child2,'name')
    sub2 = variable.SubElement(child2, 'surname')
    sub3 = variable.SubElement(child2, 'email')
    sub4 = variable.SubElement(child2, 'dni')


    child3 = variable.SubElement(r,'student')
    sub1_2 = variable.SubElement(child3, 'name')
    sub2_2 = variable.SubElement(child3, 'surname')
    sub3_2 = variable.SubElement(child3, 'email')
    sub4_2 = variable.SubElement(child3, 'dni')

    child4 = variable.SubElement(r,'student')
    sub1_3 = variable.SubElement(child4, 'name')
    sub2_3 = variable.SubElement(child4, 'surname')
    sub3_3 = variable.SubElement(child4, 'email')
    sub4_3 = variable.SubElement(child4, 'dni')

    child5 = variable.SubElement(r,'student')
    sub1_5 = variable.SubElement(child5, 'name')
    sub2_4 = variable.SubElement(child5, 'surname')
    sub3_4 = variable.SubElement(child5, 'email')
    sub4_4 = variable.SubElement(child5, 'dni')

    #guardamos el archivo xml 
    savexml = variable.ElementTree(r)
    #determinamos el nombre del archivo xml
    savexml.write("estudiantes.xml")


    #buscamos el archivo xml
    tree = variable.parse("estudiantes.xml")
    #cogemos el root del xml y lo metemos en una variable
    root = tree.getroot()
    
    #nos situamos en el primer subelemento 0
    element0 = root[0]
    child0 = root[0][0]
    child1 = root[0][1]
    child2 = root[0][2]
    child3 = root[0][3]
    element1 = root[1]
    child0_1 = root[1][0]
    child1_2 = root[1][1]
    child2_3 = root[1][2]
    child3_4 = root[1][3]
    element2 = root[2]
    child0_12 = root[2][0]
    child1_22 = root[2][1]
    child2_32 = root[2][2]
    child3_42 = root[2][3]
    element3 = root[3]
    child0_123 = root[3][0]
    child1_223 = root[3][1]
    child2_323 = root[3][2]
    child3_423 = root[3][3]
    element4 = root[4]
    child0_1234 = root[4][0]
    child1_2234 = root[4][1]
    child2_3234= root[4][2]
    child3_4234 = root[4][3]
    #insertamos los valores de los atributos
    element0.set('instituto', 'IJB')
    child0.text = 'pepito'
    child1.text = 'lombardo'
    child2.text = 'road@gmail.com'
    child3.text = '18166243A'
    element1.set('instituto', 'IES Can Mas')
    child0_1.text = 'juan'
    child1_2.text = 'garcia'
    child2_3.text = 'road@gmail.com'
    child3_4.text = '18166243A'
    element2.set('instituto', 'IES La Virgen Maria')
    child0_12.text = 'andres'
    child1_22.text = 'perez'
    child2_32.text = 'road@gmail.com'
    child3_42.text = '18166243A'
    element3.set('instituto', 'IES Sant Joan de deu')
    child0_123.text = 'javier'
    child1_223.text = 'jurado'
    child2_323.text = 'road@gmail.com'
    child3_423.text = '18166243A'
    element4.set('instituto', 'IES Escursell')
    child0_1234.text = 'luis'
    child1_2234.text = 'buñuales'
    child2_3234.text = 'road@gmail.com'
    child3_4234.text = '18166243A'
    #se escriben los cambios
    tree.write("estudiantes.xml")

    #mostrar por la consola el archivo xml
    return variable.dump(r)

crearxml()