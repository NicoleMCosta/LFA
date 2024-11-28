import random as rd
import string
import math

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
    if set_off == True:
        return #mudar o caminho possivel



num_quadras = (2,2)
num_estados = (num_quadras[0]+1)*(num_quadras[1]+1)  #começa do 1


x = 1
y = 1
estado_atual =(x,y)

num_carros = rd.randint(1,5)
# print(num_carros)

k1 = rd.randint(1,200)
rota = rd.choices('debc', k = 5) 
print(f"rota: {rota}\n{len(rota)} ")

pilha = []

# for i in range(num_carros):
#    for r in range(len(rota)):
#     pilha[i][r] = rota[r]


# print(pilha)

for path in rota:
    caminho = proximo_estado(estado_atual, path)
    if caminho == 0:
        print("\nrota impossivel")
        break
    else:
        print(caminho)
