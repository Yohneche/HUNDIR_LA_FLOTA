import random
import time
import pprint

tablero_charly = []
tablero_python = []

for i in range(10):
    linea = []
    for j in range(10):
        linea.append(" ")
    tablero_charly.append(linea)
tablero_charly

tablero_python = []

for i in range(10):
    linea = []
    for j in range(10):
        linea.append(" ")
    tablero_python.append(linea)
tablero_python

tablero_vacio_charly = []
tablero_vacio_python = []

for i in range(10):
    linea = []
    for j in range(10):
        linea.append(" ")
    tablero_vacio_charly.append(linea)

for i in range(10):
    linea = []
    for j in range(10):
        linea.append(" ")
    tablero_vacio_python.append(linea)


tablero_charly[1][0] = "B"
tablero_charly[1][1] = "B"
tablero_charly[1][2] = "B"
tablero_charly[1][3] = "B"

tablero_charly[3][3] = "B"
tablero_charly[4][3] = "B"
tablero_charly[5][3] = "B"

tablero_charly[7][1] = "B"
tablero_charly[7][2] = "B"
tablero_charly[7][3] = "B"

tablero_charly[0][7] = "B"
tablero_charly[0][8] = "B"

tablero_charly[4][7] = "B"
tablero_charly[5][7] = "B"

tablero_charly[9][0] = "B"
tablero_charly[9][1] = "B"

tablero_charly[2][9] = "B"
tablero_charly[5][5] = "B"
tablero_charly[8][8] = "B"
tablero_charly[9][9] = "B"

tablero_python[2][2] = "B"
tablero_python[3][2] = "B"
tablero_python[4][2] = "B"
tablero_python[5][2] = "B"

tablero_python[0][4] = "B"
tablero_python[0][5] = "B"
tablero_python[0][6] = "B"

tablero_python[6][7] = "B"
tablero_python[7][7] = "B"
tablero_python[8][7] = "B"

tablero_python[9][3] = "B"
tablero_python[9][4] = "B"

tablero_python[4][8] = "B"
tablero_python[5][8] = "B"

tablero_python[2][0] = "B"
tablero_python[3][0] = "B"

tablero_python[1][9] = "B"
tablero_python[3][6] = "B"
tablero_python[6][1] = "B"
tablero_python[8][4] = "B"

while True:
    while True:

        i = input("Introduzca la coordenada X, un número del 1 al 10")
        j = input("Introduzca la coordenada Y, un número del 1 al 10")

        i = (int(i) - 1)
        j = (int(j) - 1)

        if tablero_python [j] [i] == "B":
            tablero_vacio_python [j] [i] = "X"
            print("Tocado en posición " + str(i + 1) + " " + str(j + 1))
        else:
            tablero_vacio_python [j][i] = "o"
            print("Agua")
            break

    while True:

        i = random.randint(0,9)
        j = random.randint(0,9)

        if tablero_charly [j] [i] == "B":
            tablero_vacio_charly [j] [i] = "X"
            print("Tocado en posición " + str(i + 1) + " " + str(j + 1))
        else:
            tablero_vacio_charly [j][i] = "o"
            print("Agua")
            break

    pprint.pprint(tablero_vacio_python)
    print()
    pprint.pprint(tablero_vacio_charly)