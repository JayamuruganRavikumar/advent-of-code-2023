#!/usr/bin/python3

import numpy as np

sum_all = 0
data = open("test_input.txt").read().strip()
lines = data.split('\n')
grid = [[m for m in l] for l in lines]
print(grid)

#for row in range(len(grid)):
#    number = 0 
#    for col in range(len(grid[row])):
        

