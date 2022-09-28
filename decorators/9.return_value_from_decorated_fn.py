from decorators import do_twice


@do_twice
def return_greeting(name):
    print("Creating greetings")
    return f"Hi {name}"


print(return_greeting("Nazmul"))
# print(obj)