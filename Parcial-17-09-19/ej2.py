

# receta "tortilla": 
# falta_comprar = {"papa":(1,"kilos"),"huevos":(4,"unidades")}
# receta "pizza":
# falta_comprar = {"harina":(0.2,"kilos"), "orégano":(25,"gramos")}
# bife a la criolla falla

class RecetaDesconocidaError(Exception):
    pass


def lista_de_compras(mi_alacena, mis_recetas, receta):
    if receta not in mis_recetas:
        raise RecetaDesconocidaError()

    falta_comprar=dict()
    ingredientes = mis_recetas[receta]

    for ingrediente, cantidad_unidad in ingredientes.items():
        cantidad, unidad = cantidad_unidad

        if ingrediente not in mi_alacena:
            falta_comprar.setdefault(ingrediente, list())
            falta_comprar[ingrediente] = cantidad_unidad
        else:
            cantidad_actual,_ = mi_alacena[ingrediente]
            if cantidad > cantidad_actual:
                falta_comprar.setdefault(ingrediente, list())
                falta_comprar[ingrediente] = (cantidad - cantidad_actual, unidad)

    return falta_comprar


mi_alacena = {"tomate": (0.4, "kilos"), "harina": (0.3, "kilos"), "aceite":(0.5, "litros"), "huevos":(2,"unidades")}
mis_recetas = {"pizza": {"tomate":(0.25, "kilos"), "harina":(0.5,"kilos"), "aceite":(0.1, "litros"),"orégano":(25,"gramos")}, "tortilla": {"papa":(1,"kilos"),"huevos":(6,"unidades")}}

print(lista_de_compras(mi_alacena, mis_recetas, "tortilla"))
print(lista_de_compras(mi_alacena, mis_recetas, "pizza"))