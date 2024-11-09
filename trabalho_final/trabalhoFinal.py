import random as rd
import string
import math
import numpy as np

# 0   1   2   3
#   ❑   ❑   ❑
# 4   5   6   7
#   ❑   ❑   ❑
# 8   9   10  11
#   ❑   ❑   ❑
# 12  13  14  15


def proximo_estado(estado_atual, pos): #nao verifica se a via permite a movimentação, mas checa os limites da cidade
    global x
    global y

    if pos == 'd':
        if x == num_quadras[1]:
            return 0
        else:
            y+=1
    elif pos == 'e':
        if y == 1:
            return 0
        else:
            y-=1
    elif pos == 'b':
        if x == num_quadras[0]:
            return 0
        else:
            x+=1
    elif pos == 'c':
        if x == 1:
            return 0
        else:
            x-=1
    else:
        print("\nerro no random")
    
    return x,y


def semaforo(set_off):
    #set_off = numero de carros que passaram pelo semaforo
    if set_off == True:
        return #mudar o caminho possivel



num_carros = rd.randint(0,5)
num_quadras = (2,2)
num_estados = (num_quadras[0]+1)*(num_quadras[1]+1)  #começa do 1


x = 2
y = 1
estado_atual =(x,y)

rota = rd.choices('debc', k = 5)
print(f"rota: {rota} ")

#for i in range(num_carros):
#    np.array([num_carros[i],[rota]])
    #https://stackoverflow.com/questions/24832715/numpy-array-matrix-of-mixed-types

for path in rota:
    caminho = proximo_estado(estado_atual, path)
    if caminho == 0:
        print("\nrota impossivel")
        break
    else:
        print(caminho)