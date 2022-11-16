# . (a) Escribir una función Python que dada una lista personajes, con pares (personaje, serie) (indica 
# en qué serie aparece un determinado personaje), y un diccionario actua_en_personajes, con clave un 
# nombre de actor/actriz y valor una lista de personajes en los que actúa, construya (y retorne) un 
# diccionario quienes_actuan donde las claves son las series y sus valores son una lista de actores / 
# actrices que actuaron en esa serie. Hay que levantar una excepción cada vez que se hace referencia a 
# un personaje no mencionado en la lista personajes (pero hay que tener cuidado de seguir procesando 
# el resto de la información).

# el resultado debe ser el diccionario 
# quienes_actuan ['El Zorro'] = ['Juan', 'Pepe']
# quienes_actuan ['Lassie'] = ['Pepe']
# Asimismo se debe levantar una excepción KeyError porque 'Don Draper' no se encuentra en la lista de 
# personajes de entrada y otra porque 'Peggy Olson' no se encuentra en la lista de personajes de 
# entrada.

def generar_quienes_actuan(lista_personajes, actua_en_personajes):
    #Hecho casteando la lista a dict
    quienes_actuan = dict()
    dic_personaje_serie = dict(lista_personajes)

    for actor, sus_personajes in actua_en_personajes.items():
        for personaje in sus_personajes:
            try:
                serie = dic_personaje_serie[personaje]
            except KeyError:
                print(f"El personaje {personaje} no se encuentra en la lista de personajes")
            else:
                quienes_actuan.setdefault(serie, list())
                quienes_actuan[serie].append(actor)

    return quienes_actuan

# def generar_quienes_actuan_lista(lista_personajes, actua_en_personajes):
#     #Hecho usando la lista per-se
#     quienes_actuan = dict()

#     for actor, sus_personajes in actua_en_personajes.items():
#         for personaje in sus_personajes:
            
#             try:
#                 indice = lista_personajes.index((personaje, ))
#                 print(indice)
#                 # serie = lista_personajes[(personaje, "Don Diego de la Vega")]
#                 # print(serie)
#             except KeyError:
#                 print(f"El personaje {personaje} no se encuentra en la lista de personajes")
#             else:
#                 quienes_actuan.setdefault(serie, list())
#                 quienes_actuan[serie].append(actor)

#     return quienes_actuan





personajes = [('Don Diego de la Vega', 'El Zorro'), ('Bernardo', 'El Zorro'), ('Timmy Martin', 'Lassie'), ('James Kildare', 'Dr. Kildare'), ('Leonard Gillespie', 'Dr. Kildare')]
actua_en_personajes = {'Juan' : ['Don Diego de la Vega', 'Don Draper'], 'Ana' : ['Peggy Olson'], 'Pepe' : ['Bernardo', 'Timmy Martin']}
print(generar_quienes_actuan(personajes, actua_en_personajes))