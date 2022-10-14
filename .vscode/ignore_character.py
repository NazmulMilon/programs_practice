"""
def clean_string(text):
    ....
    ....
    print(output)
    
s = "I::::::D,,,,,U;;;;B,,,A--T;,:I..A"

output = clean_string(s)
print(output)

"""
import string

print('hi')
s = "I::::::DFG,,,,,U;;;;B,,,A--T;,:I..A"

letter = list(string.ascii_letters)


def clean_string(text):
    for i in text:
        if i in letter:
            print(i, end="")


# print()
clean_string(s)
print()
print('bye')
