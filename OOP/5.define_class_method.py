class Person:
    
    counter=0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter +=1

    def display(self):
        return f"Hi, I am {self.name}"

    @classmethod
    def create_something(cls):
        return Person('lll', 25)


obj = Person.create_something()
print(obj.name)
