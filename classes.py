class MyClass:
    i = 12345

    def f(self):
        return 'hello world'


print(MyClass.f)
print(MyClass.i)


class Complex:

    def __init__(self, realpart, imagpart):  # to co podane trzeba podać przy tworzeniu nowego obiektu
        self.data = []
        self.r = realpart
        self.i = imagpart


class Dog:

    kind = 'canine'  # zmienna jednakowa dla wszystkich obiektów klasy

    def __init__(self, name):
        self.name = name  # zmienna unikalna dla każdego obiektu
