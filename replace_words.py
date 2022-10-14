"""
replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia.
 Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

a = ['oh', 'Emelia', 'to']
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much.
This time we are going to Bangladesh."

output = "I love Bangladesh" (inside a file)
"""

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

ss = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
s2 = ss.split()
# print("OK")

l = len(replace_with)
s = len(s2)
print(l, s)

new_list = []


# for i, j in enumerate(s):
#     if j in replace_with:
#         # print(i)
#         print(i, j)
# print(replace_with[i])
# print('ni')
# print(replace_with)
# print('hi')
