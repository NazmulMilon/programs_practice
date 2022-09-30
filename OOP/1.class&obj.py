class Person:
    pass


obj = Person()
obj.name = "MILON"
print(obj.name)

print(callable(print))
print(callable(len))
print(callable(callable))

print('\n')


def add(a, b):
    return a+b


print(callable(add))
print(callable(lambda x: x*x))