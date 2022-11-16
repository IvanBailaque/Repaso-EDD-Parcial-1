import csv

def ordenar_por_obra(path_csv, path_salida):
    with open (path_csv, "r", encoding="utf8") as f_in, open(path_salida, "w", encoding="utf8") as f_out:
        consultas = csv.DictReader(f_in, delimiter=",")

        dic_obra_cantidad = dict()
        dic_obra_consultas = dict()

        for consulta in consultas:
            fecha, nombre, obra, codigo, tipo = consulta.values()

            dic_obra_cantidad.setdefault(obra, 0)
            dic_obra_cantidad[obra] += 1

            tupla = (fecha, nombre, codigo, tipo)
            dic_obra_consultas.setdefault(obra, list())
            dic_obra_consultas[obra].append(tupla)

        for obra, consultas in dic_obra_consultas.items():
            f_out.write(f'{obra}:\n')
            for consulta in consultas:
                consulta_a_escribir= f'{consulta[0]},{consulta[1]},{consulta[2]},{consulta[3]}'
                f_out.write(f'{consulta_a_escribir}\n')
            f_out.write(f'{obra}: Total {dic_obra_cantidad[obra]} pacientes.\n')

ordenar_por_obra("./Parcial-16-09-20/entrada.csv", "./Parcial-16-09-20/salida.txt")