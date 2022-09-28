def parent():
    print("Printing from the parent function")

    def first_child():
        print("Print from the first_child() function")

    def second_child():
        print("Print from the second_child() funciton")

    # print(second_child())
    # print(first_child())

    second_child()
    first_child()


print(parent())