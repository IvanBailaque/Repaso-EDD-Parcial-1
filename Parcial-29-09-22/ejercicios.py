import csv
import json
def ejercicio_1_version_santi(path_archivo):
    with open(path_archivo,"r", encoding="utf8") as archivo, open("prioridades.json", "w", encoding="utf8") as archivo_salida:
        
        dic_remitente_prioridades = dict()
        lector= csv.DictReader(archivo, delimiter = ",")

        for correo in lector:
            remitente = correo["Desde"]
            prioridad = correo["Prioridad"]

            prioridades_actualizadas = list()
            prioridades_actuales = dic_remitente_prioridades.setdefault(remitente, list())

            encontrado = False
            for prioridad_actual, cantidad in prioridades_actuales:
                if prioridad == prioridad_actual:
                    prioridades_actualizadas.append((prioridad_actual, cantidad + 1))
                    encontrado = True
                else:
                    prioridades_actualizadas.append((prioridad_actual, cantidad))
            if not encontrado:
                prioridades_actualizadas.append((prioridad, 1))

            dic_remitente_prioridades[remitente] = prioridades_actualizadas

        salida = {"prioridades": dic_remitente_prioridades}
        json.dump(salida, archivo_salida)

ejercicio_1_version_santi("Parcial-29-09-22/archivo.csv")

