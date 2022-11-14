import csv
import shelve

def persistir_contacto(path_archivo, path_salida):
    with open(path_archivo, "r", encoding="utf8") as f_csv, shelve.open(path_salida) as salida:
        reader = csv.DictReader(f_csv, delimiter = ";")
        for linea in reader:
            apellido = linea["apellido"]
            salida[apellido] = linea
