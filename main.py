import os
from FilaPrioridade import FilaPrioridade
from Fila import Fila

pedidosAguardando = []
pedidosPreparando = Fila()
tempoEsperaPedidosPreparando = 0

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
        print("Infome o tamanho da fila:")
        tamanhoFila = int(input())
        pedidosAguardando = FilaPrioridade(tamanhoFila)

    elif option == "2":
        print("Informe os dados do grupo que está fazendo o pedido!")
        tamanhoGrupo = input("Quantidade de pessoas: ")
        tempoPreparo = input("Tempo de preparo: ")
        nomeResponsavel = input("Nome do responsável: ")
        pedido = (tamanhoGrupo, tempoPreparo, nomeResponsavel)
        pedidosAguardando.inserir(pedido)
        
    elif option == "3":
        if len(pedidosAguardando) > 0:
            print(pedidosAguardando.proxGrupo(pedidosAguardando))
        else:
            print("Não existem pedidos aguardando!\n")
        
    elif option == "4":
        print("Responsável pelo pedido: " + (pedidosAguardando.proxGrupo(pedidosAguardando)[2])) 

        for pedido in pedidosPreparando:
            tempoEsperaPedidoAtual = pedido[1]
            tempoEsperaPedidosPreparando += tempoEsperaPedidoAtual

        print("Tempo de espera: " + (tempoEsperaPedidoAtual + tempoEsperaPedidosPreparando))

        pedidoParaPreparo = pedidosAguardando.remover(pedidosAguardando)
        pedidosPreparando.append(pedidoParaPreparo)

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