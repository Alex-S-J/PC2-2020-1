from random import randint as rd

import Numpy as np


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


def mueve_col():
    
    
    AB=np.array([(34,43,73,25,10),(82,22,12,14,10),(53,94,66,84,10),(35,73,24,34,10)])

    print(AB)