import os
import heapq
from Fila import Fila

#minHeap
pedidosAguardando = []

#queue
pedidosPreparando = Fila()

tempoEsperaPedidosPreparando = 0
inserções = 0

cadastrar = True
while cadastrar == True:
    print("#################### MENU ####################")
    print("1 - Definir tamanho da fila com prioridades\n"
        "2 - Adicionar novo grupo na fila com prioridades\n"
        "3 - Mostrar próximo grupo aguardando\n"
        "4 - Entregar refeição\n"
        "0 - Sair\n")
    print("Escolha o que você deseja fazer:")

    option = input()
    os.system("cls")

    if option == "1":
        print("Informe o tamanho da fila:")
        tamanhoFilaAguardando = int(input())        

    elif option == "2":
        if len(pedidosAguardando) < tamanhoFilaAguardando:
            print("Informe os dados do grupo que está fazendo o pedido!")
            tamanhoGrupo = input("Quantidade de pessoas: ")
            tempoPreparo = input("Tempo de preparo: ")
            nomeResponsavel = input("Nome do responsável: ")
            pedido = (tamanhoGrupo, tempoPreparo, nomeResponsavel)
            heapq.heappush(pedidosAguardando, pedido)
            inserções += 1
            print("Adicionado com sucesso!")
        else:
            print("Tamanho da fila esgotado!")
        
    elif option == "3":
        if len(pedidosAguardando) > 0:
            print(pedidosAguardando[0])
        else:
            print("Não existem pedidos aguardando!\n")
        
    elif option == "4":
        pedidoParaPreparo = heapq.heappop(pedidosAguardando)
        inserções -= 1
        pedidosPreparando.append(pedidoParaPreparo)

        for p in pedidosPreparando.list():
            tempoEsperaPedidoAtual = int(p[1])
            tempoEsperaPedidosPreparando += tempoEsperaPedidoAtual
        
        print("Responsável pelo pedido:", (pedidosPreparando[0]))
        print("Tempo de espera: " + (tempoEsperaPedidoAtual + tempoEsperaPedidosPreparando))

    elif option == "5":
        print("Pedido de: " + (pedidosPreparando.pop())[2] + ", está pronto!")
        

#6) Gerar simulação ##############################################################################################
#    a. Gerar aleatoriamente vários grupos de diferentes tamanhos, nomes e tempo de preparo e realizar a
#adição a uma fila previamente vazia, para então o usuário interagir através das opções já existentes
#no menu, sem ter que ficar digitando os dados.

    elif option == "0":
        exit()

    #caso especial
    else:
        print("Entrada inválida!")