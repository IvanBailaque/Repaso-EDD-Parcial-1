import shelve
import json

libros = {("Mining the Social Web", "M.A.Russel"): "20",("Data structures and problem solving using Java", "M.A.Weiss"): "5"}

libros_en_uso={"Estructura de datos": [("Mining the Social Web", "M.A.Russel"), ("Learning Python", "M. Lutz")], "Algoritmos 1": [("Object-Oriented Software Construction", "B.Meyer")], "Algoritmos 2": [("Data structures and problem solving using Java", "M.A.Weiss"), ("Object-Oriented Software Construction", "B.Meyer")]}

#1
def que_nos_falta(libros, libros_en_uso):
    libros_faltan = dict()

    for materia, lista_libros in libros_en_uso.items():
        for libro_autor in lista_libros:
            if libro_autor not in libros.keys():
                libros_faltan.setdefault(libro_autor, list())
                libros_faltan[libro_autor].append(materia)

    return libros_faltan

libros_faltan = que_nos_falta(libros, libros_en_uso)
print(libros_faltan)

#2 Shelve
def guardar_libros_en_disco(libros_faltan, nombre_archivo):
    with shelve.open(nombre_archivo) as archivo:
        archivo["libros faltantes"] = libros_faltan

guardar_libros_en_disco(libros_faltan, "libros_faltantes.s")

# 3 Shelve
def recuperar_libros_de_disco(nombre_archivo):
    with shelve.open(nombre_archivo) as archivo:
        libros_faltan = archivo["libros faltantes"]
        return libros_faltan

print(recuperar_libros_de_disco("libros_faltantes.s"))

# #2 Json NO SE PUEDE PQ ES CON TUPLA LA KEY DEL DIC
# def guardar_libros_en_disco_json(libros_faltan, nombre_archivo):
#     with open (nombre_archivo, "w") as archivo:
#         json.dump(libros_faltan, archivo)

# guardar_libros_en_disco_json(libros_faltan, "libros_faltantes.j")