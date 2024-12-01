import random

quintupla = {
    'alfabeto': ["c", "b", "e", "d", "p"],
    'estados': ["A", "B", "C", "D", "c1c", "c1b", "c1e", "c2e", "c2b", "c2c", "c3c", "c3b", "c3d", "c4c", "c4b", "c4d", "r2", "r3", "p1", "p2", "p3", "p4", "p5"],
    'programa': [
        [None, "c1c", None, None, "p1"],
        [None, "c2c", None, None, "p2"],
        [None, None, None, "c1e", None],
        [None, None, "c4d", None, None],
        [None, "c3c", None, "c2e", None],
        ["p1", None, None, "c2e", None],
        ["p1", "c3c", None, "c2e", None],
        ["p2", None, "c4c", "p3", None],
        ["p2", None, None, "p3", None],
        [None, 'c4c', "p3", None, None],
        [None, "r2", "p5", None, None],
        ["c1b", None, "p5", None, None],
        ["c1b", "r2", "p5", None, None],
        [None, "r3", "c3d", None, "p4"],
        ["c2b", None, "c3d", None, "p4"],
        ["c2b", "r3", "c3d", None, "p4"],
        ["c3b", None, None, None, None],
        ["c4b", None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]],
    'inicial': "A",
    'final': ["p1", "p2", "p3", "p4", "p5"]
}

semaforo = ["c2e", "c2b", "c2c", "c3c", "c3b", "c3d"]
MAXIMOPILHA = 5


class Carro:
    def __init__(self, estado_inicial):
        self.estadoAtual = estado_inicial
    @staticmethod
    def verificaSemaforo(estadoAtual: str, semaforo: list, pilha: list, MAXIMOPILHA: int):
        if estadoAtual in semaforo:
            pilha[0] += 1
            print(f"Carro em {estadoAtual}: empilhou, pilha = {pilha[0]}")
            if pilha[0] >= MAXIMOPILHA:
                pilha[0] = 0


def simulador(num_carros, quintupla, semaforo, MAXIMOPILHA):
    pilha = [0]
    carros = [Carro(quintupla['inicial']) for _ in range(num_carros)]
    estacionados = []

    for c in carros:
        print(f"\nCarro {id(c)}\n")
        while c.estadoAtual not in quintupla["final"]:
            estadoAnterior = c.estadoAtual
            while True:
                transicao = random.choice(quintupla["programa"][quintupla["estados"].index(estadoAnterior)])
                if transicao is not None:
                    c.estadoAtual = transicao
                    break

            print(f"{estadoAnterior} -> {c.estadoAtual}")
            Carro.verificaSemaforo(c.estadoAtual, semaforo, pilha, MAXIMOPILHA)

        if c.estadoAtual in quintupla["final"]:
            print(f"Carro {id(c)} chegou ao estado final: {c.estadoAtual}")
            estacionados.append(c)


num_carros = random.randint(5, 10)
simulador(num_carros, quintupla, semaforo, MAXIMOPILHA)
