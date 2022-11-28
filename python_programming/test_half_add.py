'''https://kipdf.com/python-for-rookies-a-first-course-in-programming-answers-to-selected-exercises
-s_5b2fbfcb097c478d398b47a8.html '''


# a = int(input("Enter Binary input: "))
# b = int(input("Enter Binary input: "))
#
#
# def get_sum(a, b):
#     return a ^ b
#
#
# def get_carry(a, b):
#     return a & b


def half_adder(a, b):
    Sum = a ^ b
    Carry = a & b
    return (Sum, Carry)


def test_half():
    assert half_adder(0, 0) == (0, 0)
    assert half_adder(0, 1) == (1, 0)
    assert half_adder(1, 0) == (1, 0)
    assert half_adder(1, 1) == (0, 1)
