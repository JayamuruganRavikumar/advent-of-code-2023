#!/usr/bin/python3
#Bring back the unaltered values

input_file = open("input_day1.txt", "r")
values_sum = 0

for amended_values in input_file.readlines():
    split_values = [*amended_values]
    split_digits = [str(s) for s in split_values if s.isdigit()]
    length = len(split_digits)
    if length > 1:
        old_value = int(split_digits[0]+split_digits[-1])
    else:
        old_value = int(split_digits[0]+split_digits[0])
    values_sum += old_value 

print(values_sum)

