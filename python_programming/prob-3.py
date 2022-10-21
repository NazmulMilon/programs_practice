# str1 = "I wonder how this text looks like backwards"
str1 = "Programming Hero is the best"
str3 = str1.split()
print(str3)


# final_str = ""


def reverse_str(string):
    final_str = ""
    for i in string:
        final_str += i[::-1] + " "

    return final_str


result = reverse_str(str3)
print(result.rstrip())
# print(result)


# str1 = "I wonder how this text looks like backwards"
# str3 = str1.split()
# print(str3)
#
# final_str = ""
# for i in str3:
#     final_str += i[::-1] + " "
#
# print(final_str)
# print(final_str.rstrip())
