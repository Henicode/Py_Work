               # trung  a class definition 

class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"my name is: {self.name}")
        print(f"my age is: {self.age}")
        print(f"my species is {Parrot.species}")