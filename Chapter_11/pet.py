class pets:
    pass

class Animals(pets):
    pass

class Dog(Animals):

    @staticmethod
    def bark():
        print("Bow Bow!")

d=Dog()
d.bark()
