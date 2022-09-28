from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7<=datetime.now().hour < 22:
            func()
        else:
            pass    # neighbours are asleep
    return wrapper


def say_something():
    print("something different")


say_something = not_during_the_night(say_something)

print(say_something())








# 6 5
# 0 1
# 0 2
# 2 3
# 3 0
# 4 5
# 2