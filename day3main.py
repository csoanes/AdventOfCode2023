
import numpy as np
import regex as re
with open("day3partonetestdata", 'r') as file:
    lines = [line.rstrip() for line in file]
array2d =[]
for line in lines:
    array2d.append([*line])

sum_of_parts=0

def find_number(xpos:int,ypos:int)int:

    # check back 1
    origin = array2d[xpos][ypos]
    backone = array2d[xpos][ypos-1]
    backtwo = array2d[xpos][ypos-2]
    forwardone = array2d[xpos][ypos+1]
    forwardtwo = array2d[xpos][ypos+2]
    notanumberregex =  re.compile('[@_!#$%^&*()<>?/\|}{~:.]')
    retval = 0

    if notanumberregex.search(backone) ==None:
        # potential backtwo
        if notanumberregex.search(backtwo) ==None:
            #this is the first number
            retval = -2
            one = int(backtwo)
            two = int(backone)
            three = int(origin)
        else:
            #backone is the first number
            retval = -1
            one = int(backone)
            two = int(origin)
            if notanumberregex.search(forwardone) == None:
                three = int(forwardone)
    else:
        #origin is the first number
        retval = 0
        one = int(origin)
        if notanumberregex.search(forwardone) == None:
            two = int(forwardone)
            if notanumberregex.search(forwardtwo) == None:
                three = int(forwardtwo)
    if 'three' in locals():
        retval = three+two*10+one*100
    elif 'two' in locals():
        retval = two+one*10
    else: retval = one

    return retval


#test find number
print (array2d)
print(find_number(0,2))
print(find_number(2,2))
print(find_number(4,2))
print(find_number(9,2))

def find_nearby_numbers(x,y):
    nearby_numbers = []
    #start with -1,-1
    numberregex = re.compile('[0-9]')
    if numberregex.search(array2d[x-1][y-1]):
        if find_number(array2d[x-1][y-1])  -1:
            #HERETIFF - check for numberrs that span more than one adjacent cell

