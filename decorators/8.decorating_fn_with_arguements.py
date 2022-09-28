

from decorators import do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")
    # print("JAKS")


print(greet("milon"))