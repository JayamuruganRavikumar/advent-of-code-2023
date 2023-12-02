#!/usr/bin/python3

data = open("input_day2.txt", "r")
game = 0 

for j,l in enumerate(data):
    split_data = l.split()
    #print(split_data)
    red = 0
    green = 0
    blue = 0
    i = 0
    #print(split_data)
    for i,s in enumerate(split_data):
        if s.startswith("red"):
           red = int(split_data[i-1])
           if red > 12:
               #i =0 is needed because a last draw can induce the break
               #making the loop count complete
               i = 0
               print("break")
               break
        elif s.startswith("green"):
           green = int(split_data[i-1])
           if green > 13:
               i=0
               print("break")
               break
        elif s.startswith("blue"):
            blue = int(split_data[i-1])
            if blue > 14:
               i = 0
               print("break")
               break
#    print(j)
    #If all the balls are within 12, 13, 14 in the bag then the loop count will
    #be equal to the lenght of the list
    if i+1 == len(split_data):
        game += j+1
        print(game)

print(game)






