
with open("day2data", 'r') as file:
    lines = [line.rstrip() for line in file]

sum_of_possible_games = 0
sum_of_powers = 0
for line in lines:
    possible =True
    red=0
    green=0
    blue=0
    power=0
    print(line)
    gameidstring = line.split(':')[0]
    gameid=gameidstring.split(' ')[-1]
    print ('Game id: {0}'.format(gameid));
    hands = line.split(':')[-1]

    for hand in hands.split(';'):
        for colourhand in hand.split(','):
            print (colourhand.strip())
            numbertext = colourhand.strip().split(' ')[0]
            colour = colourhand.strip().split(' ')[-1]
            number = int(numbertext)
            print (number, colour)
            if (colour =='red'):
                if number > 12:
                    print("Invalid game!", gameid)
                    possible = False
                if (number > red):
                    red = number
            elif (colour =='green'):
                if number > 13:
                    print("Invalid game!", gameid)
                    possible = False
                if (number > green):
                    green = number
            elif (colour == 'blue'):
                if number > 14:
                    print("Invalid game!", gameid)
                    possible = False
                if (number > blue):
                    blue = number
    if (possible==True):
        sum_of_possible_games+=int(gameid)
    sum_of_powers += red*blue*green
print (sum_of_possible_games)
print (sum_of_powers)