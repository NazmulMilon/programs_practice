
class A():
    def disp(self):
        print("A disp()")


class B(A):
    pass


obj = B()
obj.disp()


# def fn(x):
#     try:
#         print(5/x)
#     except ZeroDivisionError:
#         print('Except Block')
#     else:
#         print('Else Block')
#     finally:
#         print('finally Block')
#
#
#
# fn(0)