class Colas:
    def __init__(self):
        self.items = []
        self.items2 = []
        self.total = []
    def encolar(self, item, item2):
        self.items.append(item)
        self.items2.append(item2)
        self.total.append(item + item2)
        print(f"Encolando para cola1: {item}")
        print(f"Encolando para cola2: {item2}")
        print(f"La primera cola: ", self.items)
        print(f"La segunda cola: ", self.items2)
    def desencolar(self):
        try:
            item = self.items.pop(0)
            item2 = self.items2.pop(0)
            total = self.total.pop(0)
            print(f"Desencolando para cola1: {item}")
            print(f"Desencolando para cola2: {item2}")
            print(f"La primera cola: ", self.items)
            print(f"La segunda cola: ", self.items2)
            print(f"La suma de {item} y {item2} es {total}")
            return item, item2, total
        except:
            raise ValueError("La cola esta vacia")
    def vacia(self):
        return self.items == []

Mi_objeto = Colas()

Mi_objeto.encolar(3,6)
Mi_objeto.encolar(4,2)
Mi_objeto.encolar(2,9)
Mi_objeto.encolar(8,11)
Mi_objeto.encolar(12,3)

Mi_objeto.desencolar()
Mi_objeto.desencolar()
Mi_objeto.desencolar()
Mi_objeto.desencolar()
Mi_objeto.desencolar()
