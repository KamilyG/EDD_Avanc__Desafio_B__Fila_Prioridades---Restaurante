import heapq

class FilaPrioridade:
    
    def __init__(self):
        #lista
        self._vet = [None]
        #MinHeap da lista
        heapq.heapify(self._vet)

    def inserir(fila, tupla):
        heapq.heappush(fila, tupla)

    def proxGrupo(self, fila):
        return fila[0]

    def remover(self, fila):
        #print do terceiro campo do elemento(no pedido é o nome), do primerio elemento da fila(o menor e que vai sair)
        heapq.heappop(fila)