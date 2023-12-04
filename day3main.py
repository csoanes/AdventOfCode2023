
import numpy as np
import regex as re
with open("Day3data", 'r') as file:
    lines = [line.rstrip() for line in file]
array2d =[]
for line in lines:
    array2d.append([*line])

part_numbers = []
ratios = []
notanumberregex =  re.compile('[^0-9]')
notasymbolregex = re.compile('[^0-9.]')

def find_number(xpos:int,ypos:int):

    # check back 1
    origin = array2d[xpos][ypos]
    backone = array2d[xpos][ypos-1]
    backtwo = array2d[xpos][ypos-2]
    forwardone = array2d[xpos][ypos+1]
    forwardtwo = array2d[xpos][ypos+2]


    if notanumberregex.search(backone) ==None:
        # potential backtwo
        if notanumberregex.search(backtwo) ==None:
            #this is the first number
            one = int(backtwo)
            two = int(backone)
            three = int(origin)
            array2d[xpos][ypos - 2]='.'
            array2d[xpos][ypos - 1]='.'
            array2d[xpos][ypos]='.'
        else:
            #backone is the first number
            one = int(backone)
            two = int(origin)
            array2d[xpos][ypos - 1] = '.'
            array2d[xpos][ypos] = '.'
            if notanumberregex.search(forwardone) == None:
                three = int(forwardone)
                array2d[xpos][ypos + 1]='.'
    else:
        #origin is the first number
        one = int(origin)
        if notanumberregex.search(forwardone) == None:
            two = int(forwardone)
            array2d[xpos][ypos + 1]='.'
            if notanumberregex.search(forwardtwo) == None:
                three = int(forwardtwo)
                array2d[xpos][ypos + 2]='.'
    if 'three' in locals():
        retval = three+two*10+one*100
    elif 'two' in locals():
        retval = two+one*10
    else: retval = one

    return retval


#test find number
print (array2d)
# print(find_number(0,2))
# print(find_number(2,2))
# print(find_number(4,0))
# print(find_number(9,2))


def find_adjacent_numbers(xpos:int, ypos:int, symbol:str):
    locations = {
        'above_left': (xpos - 1, ypos - 1),
        'above': (x-1, ypos),
        'above_right': (xpos-1, ypos+1),
        'left': (xpos,ypos-1),
        'origin': (xpos, ypos),
        'right':  (xpos, ypos+1),
        'below_left':  (xpos+1, ypos-1),
        'below':  (xpos+1, ypos),
        'below_right':  (xpos+1, ypos+1),
    }
    gear_ratios = []
    for location in locations:
        locx = locations[location][0]
        locy = locations[location][1]
        print(f'Checking {location}:({locx},{locy} ({array2d[locx][locy]})')
        if (notanumberregex.search(array2d[locx][locy])) ==None:
            part_number = find_number(locx, locy)
            part_numbers.append(part_number)
            if (symbol=='*'):
                gear_ratios.append(part_number)
            print(f'parts: {part_numbers}')
            print(f'ratios: {gear_ratios}')
    if (symbol=='*' and len(gear_ratios)>1):
        ratios.append(np.array(gear_ratios).prod())

xmax = len(array2d)
ymax = len(array2d[0])

for x in range(xmax):
    for y in range(ymax):
        print (f'Checking {x},{y} for symbol')
        if notasymbolregex.search(array2d[x][y]) ==None:
            continue
        print (f'Symbol_found at ({x},{y}): {array2d[x][y]}' )
        find_adjacent_numbers(x, y, array2d[x][y])

print (np.array(part_numbers).sum())
print (ratios)
print (np.array(ratios).sum())