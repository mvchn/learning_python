class Animal:
    def __init__(self, name):
        self.name = name


class Duck(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.is_watered = False

    def get_name(self):
        return f"{self.name} {self.color}"

    def swim(self):
        self.is_watered = True

    def get_watered(self):
        return self.is_watered

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap!')


ducky = Duck('Ducky', 'white')

print(ducky.get_name())

print(ducky.get_watered())

if not ducky.get_watered():
    ducky.swim()

print(ducky.get_watered())





