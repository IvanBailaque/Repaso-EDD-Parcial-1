import csv

class CodigoLibroError(Exception):
    def _init_(self):
        super()

def completar_datos_libro(csv_entrada, csv_salida, dic_libros):
    with open (csv_entrada, "r", encoding="utf8") as f_in, open(csv_salida, "w", encoding="utf8") as f_out:
        reader_in = csv.DictReader(f_in, delimiter = ",")

        campos = ("Docente", "Curso", "Nombre Libro", "Autor")
        writer_out = csv.DictWriter(f_out, fieldnames= campos, delimiter = ",")
        writer_out.writeheader()

        for linea in reader_in:
            try:
                docente, curso, codigo = linea["Docente"],linea["Curso"], linea["Codigo Libro"]

                nombre, autor = buscar_codigo(dic_libros, codigo)

                writer_out.writerow({"Docente": docente, "Curso": curso, "Nombre Libro": nombre, "Autor" : autor})

            except CodigoLibroError:
                print(f'El codigo {codigo} no se encuentra en el diccionario')
                continue

def buscar_codigo(dic_libros, codigo):
    if codigo not in dic_libros:
        raise CodigoLibroError()

    return dic_libros.get(codigo)

if __name__ == '__main__':
    diccionario_libros = {"20": ("Mining the Social Web", "M.A.Russel"), "5":("Data structures and problem solving using Java", "M.A.Weiss")}
    completar_datos_libro("Parcial-14-11-17/csv_entrada.csv", "csv_salida", diccionario_libros)
