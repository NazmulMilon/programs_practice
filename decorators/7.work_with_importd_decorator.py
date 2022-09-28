
from decorators import do_twice


@do_twice
def say_something():
    print("Looks good using decorator")


print(say_something())

