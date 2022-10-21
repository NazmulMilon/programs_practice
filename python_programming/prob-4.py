
# x = 'x3b5y4z5U3'
x = 'x3b4U5i2'
# bbbbiiUUUUUxxx

y = list(x)
# y.sort()
# print(y)

final_list = []
for key, char in enumerate(y):
    if key % 2 != 0:
        z = int(y[key])
        final_list.append(y[key-1] * z)


print(final_list)
final_list.sort(key=str.lower)

final_str = ""
for word in final_list:
    final_str += word
print(final_str)


z = int(y[1])
print(type(z))

print(y[0] * z)

# x3b5y4z5U3