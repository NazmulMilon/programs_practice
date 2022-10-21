a, b, c = map(float, input('Enter numbers: ').split('-'))


def sum_fn(n1, n2, n3):
    return n1 + n2 + n3


result = sum_fn(a, b, c)
print('Sum is:', result)
