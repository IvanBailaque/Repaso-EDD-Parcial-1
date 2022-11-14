import os
import csv

class AgendaException(Exception):
    "excepcion"

class AgendaCSV:
    def __init__(self, archivo, *campos):
        self._archivo = archivo
        self._campos = campos
        try:
            os.path.getsize(archivo)
        except FileNotFoundError:
            with open (archivo, "w", newline="", encoding="utf8") as datos:
                writer = csv.DictWriter(datos, fieldnames=campos, delimiter = ";")
                writer.writeheader()

    def guardar_contacto(self, **datos):
        if len(datos) != len(self._campos):
          raise AgendaException
        for campo, dato in datos:
            if campo not in self._campos:
                raise AgendaException()
            if dato.strip() == "":
                raise AgendaException()

        with open(self._archivo, "a",newline="", encoding="utf8") as archivo:
            writer=csv.DictWriter(archivo, fieldnames=self._campos, delimiter = ";")
            
            writer.writerow(datos)