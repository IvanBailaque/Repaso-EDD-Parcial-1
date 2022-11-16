import csv

def ayudar_edd(path_entrada, path_salida):
    with open (path_entrada, "r", encoding="utf8") as f_in, open(path_salida, "w", encoding="utf8") as f_out:
        reader_in = csv.DictReader(f_in, delimiter=",")

        campos = ("Nombre","Padron","Parcial 1","Recup 1","Parcial 2","Recup 2","Estado TP1 (A,I,Falta)","Estado TP2 (A,1,Falta)","Puede dar final (Si,No)", "Promociono (Si, No)", "Nota de promocion")

        writer_out = csv.DictWriter(f_out,fieldnames=campos,delimiter=",")
        writer_out.writeheader()

        for alumno in reader_in:
            nombre, padron, parcial_1, recup_1, parcial_2, recup_2, tp1, tp2 = alumno.values()
            
            nota_1 = max(float(parcial_1 or 0), float(recup_1 or 0))
            nota_2 = max(float(parcial_2 or 0), float(recup_2 or 0))
            
            if nota_1 >=7 and nota_2 >= 7 and tp1 =="A" and tp2 == "A":
                linea = {"Nombre":nombre, "Padron":padron, "Parcial 1":parcial_1, "Recup 1":recup_1, "Parcial 2":parcial_2, "Recup 2":recup_2, "Estado TP1 (A,I,Falta)":tp1, "Estado TP2 (A,1,Falta)":tp2, "Puede dar final (Si,No)":"Si", "Promociono (Si, No)":"Si", "Nota de promocion":(nota_1+nota_2)/2}
                writer_out.writerow(linea)
            elif nota_1 >= 4 and nota_2 >=4 and tp1 == "A" and tp2 == "A":
                linea = {"Nombre":nombre, "Padron":padron, "Parcial 1":parcial_1, "Recup 1":recup_1, "Parcial 2":parcial_2, "Recup 2":recup_2, "Estado TP1 (A,I,Falta)":tp1, "Estado TP2 (A,1,Falta)":tp2, "Puede dar final (Si,No)":"Si", "Promociono (Si, No)":"No"}
                writer_out.writerow(linea)
            else :
                linea = {"Nombre":nombre, "Padron":padron, "Parcial 1":parcial_1, "Recup 1":recup_1, "Parcial 2":parcial_2, "Recup 2":recup_2, "Estado TP1 (A,I,Falta)":tp1, "Estado TP2 (A,1,Falta)":tp2, "Puede dar final (Si,No)":"No", "Promociono (Si, No)":"No"}
                writer_out.writerow(linea)
            
ayudar_edd("./Parcial 17-09-19/entrada.csv","./Parcial 17-09-19/salida.csv")