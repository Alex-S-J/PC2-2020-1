from random import randint as rd


A=int(input("Ingrese el numero de filas: "))

B=int(input("Ingrese el numero de columnas: "))

def crea_arreglo (A,B):

    AB=[]
    for i in range (A):
        AB.append([]*B)

    for i in range (A):
        for j in range (B):
            AB[i].append(rd(0,100))

    Cad=""
    for i in range(A):
        for j in range(B):
            Cad = Cad+"\t"+str(AB[i][j])
        Cad = Cad+"\n"
    return Cad
print(str(crea_arreglo(A,B)))