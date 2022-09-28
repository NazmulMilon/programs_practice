
def my_decorator(func):
    def wrapper():
        print("Something is happening before function call")
        func()
        print("Something happening after the function call")
    return wrapper


def say_something():
    print("saying something about decorator! ")


say_something = my_decorator(say_something)
# print(say_something())
# print(my_decorator(say_something))

print(say_something())
