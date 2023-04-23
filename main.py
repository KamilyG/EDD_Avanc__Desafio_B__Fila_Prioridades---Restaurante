import os
import heapq
from Fila import Fila


#minHeap
pedidosAguardando = []

#queue
pedidosPreparando = Fila()

tamanhoFilaAguardando = 0
inserções = 0

def tempoEspera(lista):
    tempoEsperaPedidosPreparando = 0
    for p in lista:
        tempoEsperaPedidosPreparando += int(p[1])
    return tempoEsperaPedidosPreparando

cadastrar = True
while cadastrar == True:
    print("#################### MENU ####################")
    print("1 - Definir tamanho da fila com prioridades\n"
        "2 - Adicionar novo grupo na fila com prioridades\n"
        "3 - Mostrar próximo grupo aguardando\n"
        "4 - Preparar refeição\n"
        "5 - Entregar refeição\n"
        "6 - Gerar Simulação\n"
        "0 - Sair\n")
    print("Escolha o que você deseja fazer:")

    option = input()
    os.system("cls")


    #Definir tamanho da fila com prioridades
    if option == "1":
        if tamanhoFilaAguardando > 0:
            print("Tamanho da fila já foi informado!\n")
        else:
            print("Informe o tamanho da fila:")
            tamanhoFilaAguardando = int(input())

        #Adicionar novo grupo na fila com prioridades
    elif option == "2":
        if len(pedidosAguardando) < tamanhoFilaAguardando:
            print("Informe os dados do grupo que está fazendo o pedido!\n")

            tamanhoGrupo = int(input("Quantidade de pessoas: "))
            tempoPreparo = int(input("Tempo de preparo: "))
            nomeResponsavel = str(input("Nome do responsável: "))

            pedido = (tamanhoGrupo, tempoPreparo, nomeResponsavel)

            heapq.heappush(pedidosAguardando, pedido)
            inserções += 1
            print("Adicionado com sucesso!\n")

        else:
            print("Tamanho da fila esgotado!\n")
        

    #Mostrar próximo grupo aguardando
    elif option == "3":
        if len(pedidosAguardando) > 0:
            print(pedidosAguardando[0])
        else:
            print("Não existem pedidos aguardando!\n")
        

    #Preparar refeição
    elif option == "4":
            if len(pedidosAguardando) > 0:
                pedidoParaPreparo = heapq.heappop(pedidosAguardando)
                pedidosPreparando.append(pedidoParaPreparo)
                inserções -= 1
    
                print("Responsável pelo pedido:", (pedidosPreparando.__getitem__(0))[2])
                print("Tempo de espera:", (tempoEspera(pedidosPreparando)))
            else:
                print("Não existem pedidos para preparar!\n")


    #Entregar refeição
    elif option == "5":
        if len(pedidosPreparando) > 0:
            print("Pedido de:", (pedidosPreparando.pop())[2] + ", está pronto!\n")
        else:
            print("Não existem pedidos prontos!\n")
    
    #Simulação previamente pronta    
    elif option == "6":
        tamanhoFilaAguardando = 10
        if len(pedidosAguardando) < tamanhoFilaAguardando:
            pedido =  (3, 30, "Carla")
            heapq.heappush(pedidosAguardando, pedido)
            pedido =  (4, 40, "Diego")
            heapq.heappush(pedidosAguardando, pedido)
            pedido =  (6, 60, "João")
            heapq.heappush(pedidosAguardando, pedido)
            pedido =  (1, 10, "Maria")
            heapq.heappush(pedidosAguardando, pedido)   
            pedido =  (3, 30, "Anderson")
            heapq.heappush(pedidosAguardando, pedido)
            pedido =  (4, 40, "Maiara")
            heapq.heappush(pedidosAguardando, pedido)
            pedido =  (6, 60, "Jorge")
            heapq.heappush(pedidosAguardando, pedido)
            pedido =  (1, 10, "Tânia")
            heapq.heappush(pedidosAguardando, pedido)       
        else:
            print("Tamanho da fila esgotado!\n")   

                           
    elif option == "0":
        exit()

    #caso especial
    else:
        print("Entrada inválida!")