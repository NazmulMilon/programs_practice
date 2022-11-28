lst = [10, 12, 23, 23, 16, 23, 21]
len_of_lst = len(lst)
total = 0
for i in lst:
    total += i
print(total)
mean = total / len_of_lst
print('Mean deviation is- ', mean)

total_sd = 0
for sd in lst:
    print(((sd - mean) ** 2))
    total_sd += ((sd - mean) ** 2)
print(total_sd)

standard_deviation = total_sd / len_of_lst
print(f"standard deviation = {standard_deviation}")

print(f"final_deviation = ", standard_deviation ** (1 / 2))
