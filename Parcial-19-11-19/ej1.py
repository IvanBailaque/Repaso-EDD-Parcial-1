import csv

def organizar_liquidacion(path_entrada):
    with open (path_entrada, "r", encoding="utf8") as f_in:
        liquidaciones = csv.DictReader(f_in, delimiter=",")
        pago_sueldo_total_sector = dict()

        for liquidacion in liquidaciones:
            _, sueldo, _, sector = liquidacion.values()
            sueldo = int(sueldo)
            pago_sueldo_total_sector.setdefault(sector, 0)
            pago_sueldo_total_sector[sector] += sueldo
    return pago_sueldo_total_sector

print(organizar_liquidacion("./Parcial-19-11-19/entrada.csv"))