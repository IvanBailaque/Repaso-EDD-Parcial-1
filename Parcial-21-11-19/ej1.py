import csv

def generar_consumos(path_entrada):
    with open (path_entrada, "r", encoding="utf8") as f_in:
        consumos = csv.DictReader(f_in, delimiter=",")

        producto_mes_cantidad = dict()

        for consumo in consumos:
            mes, _, producto, cantidad = consumo.values()
            cantidad = float(cantidad)

            nuevos_consumos = list()

            consumos_actuales = producto_mes_cantidad.setdefault(producto, list())
            
            encontrado = False
            for mes_actual, cantidad_actual in consumos_actuales:
                if mes_actual == mes:
                    cantidad_actual = float(cantidad_actual)
                    nuevos_consumos.append((mes_actual, cantidad_actual + cantidad))
                    encontrado = True
                else:
                    nuevos_consumos.append((mes_actual, cantidad_actual))
            if not encontrado:
                nuevos_consumos.append((mes, cantidad))
                
            producto_mes_cantidad[producto] = nuevos_consumos
        
        print(producto_mes_cantidad)

generar_consumos("./Parcial-21-11-19/ej1.csv")