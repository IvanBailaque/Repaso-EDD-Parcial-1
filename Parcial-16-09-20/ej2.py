import shelve

def armar_lista_compras(recetas, alacena, que_se_cocina):
    lista_compras = dict()

    for plato, porcion in que_se_cocina:
        ingredientes = recetas[plato]
        for ingrediente, cantidad in ingredientes:
            cantidad_requerida = cantidad * porcion

            if ingrediente in alacena:
                cantidad_actual = alacena.get(ingrediente)

                if cantidad_requerida >= cantidad_actual:
                    lista_compras.setdefault(ingrediente, 0)
                    lista_compras[ingrediente] += cantidad_requerida
            else:
                lista_compras.setdefault(ingrediente, 0)
                lista_compras[ingrediente] += cantidad_requerida

    for ingrediente, cantidad in lista_compras.items():
        if ingrediente in alacena:
            cantidad_actual = alacena[ingrediente]
            lista_compras[ingrediente]-= cantidad_actual

    return lista_compras

def persistir_diccionarios(dic):
    with shelve.open("./Parcial-16-09-20/diccionarios.s") as archivo:
        archivo["dic"] = dic

        
def recuperar_diccionarios(path_archivo):
    with shelve.open(path_archivo) as archivo:
        return archivo["dic"]



recetas = {"pizza": [("harina", 30),("tomate",1),("queso", 25)], "ensalada":[("lechuga",100),("tomate", 1),("zanahoria", 1)], "flan":[("huevo", 1), ("leche", 100),("azucar", 60)]}
alacena= {"huevo": 6, "harina": 500, "queso":250, "tomate":2}
que_se_cocina = [("pizza", 4),("ensalada",2)]
lista_compras = armar_lista_compras(recetas, alacena, que_se_cocina)

# persistir_diccionarios(recetas)
print(recuperar_diccionarios("./Parcial-16-09-20/diccionarios.s"))