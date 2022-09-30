class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter +=1

    def display(self):
        return f"Hi, I am {self.name}"


# print(Person.counter)
#
# person = Person('Milon', 25)
# print(person.display())

person1 = Person("Nazmul", 26)
person2 = Person("Milon", 22)
person3 = Person("Milu", 21)
print(Person.counter)