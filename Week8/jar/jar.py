class Jar:
    def __init__(self, capacity=12): #defino el argumento de la clase. constructor
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self.size # lo que me imprimira, ademas con una operación

    def deposit(self, n): # deposit recibe un argumento que sera un numero
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError
        self._size += n # aca se sumara a con size y ese sera deposit

    def withdraw(self, n): # esto es lo que estraigo
        if n > self.size:
            raise ValueError
        self._size -= n # y se resta de size

    @property
    def capacity(self): # decoradores para definir
        return self._capacity

    @property
    def size(self):
        return self._size
def main():
    jar = Jar(4)
    jar.deposit(2)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()

