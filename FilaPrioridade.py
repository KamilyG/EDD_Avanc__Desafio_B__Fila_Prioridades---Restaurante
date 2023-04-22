import heapq

class FilaPrioridade:
    
    def __init__(self, size):
        #lista
        self._vet = [None] * size
        #contador
        self.size = size
        #MinHeap da lista
        filaPrioridade = heapq.heapify(self._vet)

    def inserir(self, tupla):
        if self.size == self._vet:
            return print("Fila está lotada!")
        else:
            heapq.heappush(self, tupla)
            self.size = self.size + 1
            return print("Adicionado com sucesso!")

    def proxGrupo(self, fila):
        return fila[0]

    def remover(self, fila):
        #print do terceiro campo do elemento(no pedido é o nome), do primerio elemento da fila(o menor e que vai sair)
        heapq.heappop(fila)
        self.size = self.size - 1