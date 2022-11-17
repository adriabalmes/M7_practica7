import json
def imprimeLibros ():
    libros = {"books":[
        {"title":"Alibaba y los 40 ladrones","cover":"Roja", "year":"1975", "pages":"320"},
        {"title":"La Ratita Presumida","cover":"Rosa", "year":"1980", "pages":"80"},
        {"title":"Caperucita Roja","cover":"Verde", "year":"1985", "pages":"120"},
        {"title":"Fray Perico y su borrico","cover":"Azul", "year":"1990", "pages":"450"},
    ]}

    with open ("jsonFile.json", 'w') as file:
        json.dump(libros,file)

    print(json.dumps(libros,indent=2))

def imprimeLibros2 ():
    with open ("jsonFile.json", 'r') as file:
        libros = json.load(file)
        print(libros)