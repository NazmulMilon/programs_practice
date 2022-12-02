# https://refactoring.guru/design-patterns/observer/python/example
from distlib.compat import raw_input
#
# file = open("words.dat", "w")
# word = ""
# i = 1
# while True:
#     word = raw_input("Enter a word('enter END to quit'):")
#     if word == "":
#         exit()
#         file.close()
#     else:
#         # file.write(str(i) + ': ')
#         file.write(str(i) + ': ' + word + "\n")
#         i += 1
# file.close()




# file = open("words.dat", "w")
# word = ""
# i = 1
# while word != "END":
#     word = raw_input("Enter a word('enter END to quit'):")
#     if word == "END":
#         exit()
#         file.close()
#     else:
#         # file.write(str(i) + ': ')
#         file.write(str(i) + ': ' + word + "\n")
#         i += 1
# file.close()




file = open("words.dat", "w")
word = ""
i = 1
while word != "END":
    word = raw_input("Enter a word('enter END to quit'):")
    # file.write(str(i) + ': ')
    file.write(str(i) + ': ' + word + "\n")
    i += 1
file.close()

file_open = open("words.dat", "r")
content = file_open.read()
print(content)
