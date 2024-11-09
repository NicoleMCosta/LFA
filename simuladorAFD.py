#simulador AFD
#quintupla: alfabeto, estados, estado inicial, estados finais, transições/função

print('''--------SIMULADOR DE AFD-------\n
      ATENÇÃO: Informe os valores separados por espaço, no caso de uma transição SEM SAÍDA prencha com \\.\\
      Exemplo:

      Linguagem: a b c
      Estados: q1 q2
      Inicial: q1
      Finais: q1 q2

      Transições:
            q1 --a--> q2
            q1 --b--> .
            q2 --a--> q2
            q2 --b--> q2
      \n''')

alfabeto = []
alfabeto.extend(input("Alfabeto: ").split())

estados = []
estados.extend(input("Estados: ").split())

inicial = input("Estado Inicial: ")

finais = []
finais.extend(input("Estados finais: ").split())

print("Transições:")
transicao = {}
for estado in estados:
    for simbolo in alfabeto:
        next = input(f"{estado} --{simbolo}--> ")
        if next == '.':
            transicao[(estado, simbolo)] = None
        else:
            transicao[(estado, simbolo)] = next
        
print("\nAlfabeto:", end=' ')
print(alfabeto)

print("Estados:", end=' ')
print(estados)

print(f"Estado Inicial: {inicial}")

print("Estados Finais:", end=' ')
print(finais)


fita = input("Informe uma palavra: ")
sucess = 1
atual = inicial
for simbolo in fita:
    if simbolo not in alfabeto:
        sucess=0
        break

    atual = transicao[(atual,simbolo)]
    if atual == None:
        sucess = 0
        break

if atual in finais and sucess == 1 :
    print("O automato reconheceu a Linguagem")
else:
    print("O automatao NÃO RECONHECEU a Linguagem")