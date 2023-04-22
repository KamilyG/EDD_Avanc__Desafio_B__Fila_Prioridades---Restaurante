class Fila:    
    def __init__(self):
        self._vet = []
    
    def append(self, item): # enfileirar
        self._vet.append(item)
    
    def pop(self): # desenfileirar
        if not self.is_empty():
            return self._vet.pop(0)

    def front(self): # mostrar o 1o da fila, sem remover!
        return self._vet[0]
                
    def is_empty(self): # retorna se a fila esta vazia
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): # representacao da fila como string
        return str(self._vet)
    
    def list(self): # representacao da fila como Lista
        return (self._vet)