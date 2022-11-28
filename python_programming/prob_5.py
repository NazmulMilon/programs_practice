all_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
week_list = []

for daily_rainfall in range(len(all_days)):
    # print(daily_rainfall)
    daily_rainfall = int(input(f"Enter rainfall for {all_days[daily_rainfall]}: "))
    week_list.append(daily_rainfall)

max_val = week_list[0]
max_day = 0


for key, val in enumerate(week_list):
    if val > max_val:
        max_val = val
        max_day = key
print(f"\nThe maximum rainfall of the week was: {max_val} mm on {all_days[max_day]}")

min_val = week_list[0]
min_day = 0
for key, val in enumerate(week_list):
    if val < min_val:
        min_val = val
        min_day = key

print(f"The minimum rainfall of the week was: {min_val} mm on {all_days[min_day]}")

total_rainfall = 0
no_of_days = len(all_days)
for rainfall in week_list:
    total_rainfall += rainfall

mean_value = total_rainfall/no_of_days
print(f"The mean deviation of rainfall is: {mean_value}")

total_sd_rainfall = 0
for st_dev in week_list:
    total_sd_rainfall += ((st_dev-mean_value)**2)
# print(f"Total st val = {total_sd_rainfall}")

standard_deviation = total_sd_rainfall / no_of_days
print(f"Standard deviation of rainfall is: ", standard_deviation **(1/2))