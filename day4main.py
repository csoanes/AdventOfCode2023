import numpy as np
import regex as re
with open("day4data", 'r') as file:
    lines = [line.rstrip() for line in file]

print (lines)

total_points = 0

for line in lines:
    points =0
    cardIdString = line.split(':')[0]
    numbersString = line.split(':')[1]
    cardId = cardIdString.split(' ')[-1]
    print (cardIdString)
    playnumbers = numbersString.split('|')[0]
    winningnumbers = numbersString.split('|')[1]

    np_playnumbers = np.fromstring(playnumbers, dtype=int, sep=' ')
    np_winningnumbers = np.fromstring(winningnumbers, dtype=int, sep=' ')

    print (np_playnumbers)
    print (np_winningnumbers)
    common = np.intersect1d(np_playnumbers, np_winningnumbers)
    for match in common:
        if (points==0): points=1
        else: points = points*2
    print (points)
    total_points += points

print (total_points)
