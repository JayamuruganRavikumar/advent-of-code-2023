#!/usr/bin/python3

data = open("input_day2.txt", "r")
power = 0 
sum_all = 0

for j,l in enumerate(data):
    split_data = l.split()
    red = 0
    green = 0
    blue = 0
    i = 0
    for i,s in enumerate(split_data):
        if s.startswith("red"):
           red_i = int(split_data[i-1])
           #find the greatest of all red, green and blue marble which
           #should be the minumim required to play the game
           if red <= red_i:
               red = red_i
        elif s.startswith("green"):
           green_i = int(split_data[i-1])
           if green <= green_i:
               green = green_i
        elif s.startswith("blue"):
           blue_i = int(split_data[i-1])
           if blue <= blue_i:
               blue = blue_i
    #print(f'{red} {green} {blue}')
    power = red*blue*green
    sum_all += power


print(sum_all)





