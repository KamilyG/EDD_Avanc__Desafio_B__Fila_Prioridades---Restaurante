"""
Para quaisquer grupos que possuem a mesma quantidade de pessoas, é priorizado o grupo cujas refeições são preparadas mais rapidamente. Considere que o restaurante possui apenas 1 cozinha e as refeições são preparadas de forma sequencial.

FILA 1: Fila com Prioridades (onde são acumulados os pedidos a serem preparados)
FILA 2: Fila FIFO (onde são armazenados os pedidos que estão em preparo)

Como o objetivo é classificar pelo menor, podemos utilizar a classe heapq presente no Python.
Confira exemplo no tópico ‘Árvores Heap’ -> ‘Python - Implementação MinHeap (nativa)’
Você também precisará de uma fila comum (FIFO), de modo que poderá usar o tipo List do Python e os
métodos: append [inserir] e pop(0) [remover o 1º da fila].

Cada item dentro da fila com prioridades deverá ser representado por uma tupla com o padrão:
(quantidade de pessoas [int], tempo de preparo [int], nome da reserva [str])

"""