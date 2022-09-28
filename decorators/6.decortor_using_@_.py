

def my_decorator(func):
    def wrapper():
        print("Something happening before function")
        func()
        print("Something is happening after function")
    return wrapper


@my_decorator
def say_something():
    print("Hey, print something ")


print(say_something())