

def parent(num):
    def first_child():
        return "Hi, I am Milon"

    def second_child():
        return "Hi, I am Nahid"

    if num == 1:
        return first_child()
    else:
        return second_child()

    # without parenthesis it will print the refernce of the first_child and second_child function.
    # if num == 1:
    #     return first_child
    # else:
    #     return second_child


print(parent(1))
# print(parent(1))