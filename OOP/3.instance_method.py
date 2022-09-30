class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Hi, I am {self.name}"


person = Person("Milon", 26)
print(person.display())