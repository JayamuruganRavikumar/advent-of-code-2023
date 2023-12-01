#!/usr/bin/python3

input_file = open("input_day1.txt", "r")

values_sum = 0
for amended_values in input_file.readlines():
    split_digits = []
    for i,c in enumerate(amended_values):
        if c.isdigit():
            split_digits.append(c)

        for f,words in enumerate(["one","two","three","four","five","six","seven","eight","nine"]):
            if amended_values[i:].startswith(words):
                split_digits.append(str(f+1))
    old_value = int(split_digits[0] + split_digits[-1])
    #print(old_value)
    values_sum += old_value
print(values_sum)


