
with open("day2data", 'r') as file:
    lines = [line.rstrip() for line in file]

sum_of_possible_games = 0
for line in lines:
    possible =True
    print(line)
    gameidstring = line.split(':')[0]
    gameid=gameidstring.split(' ')[-1]
    print ('Game id: {0}'.format(gameid));
    hands = line.split(':')[-1]

    for hand in hands.split(';'):
        for colourhand in hand.split(','):
            print (colourhand.strip())
            number = colourhand.strip().split(' ')[0]
            colour = colourhand.strip().split(' ')[-1]
            print (number, colour)
            if (colour =='red' and int(number) > 12):
                print("Invalid game!", gameid)
                possible = False
            elif (colour =='green' and int(number) > 13):
                print("Invalid game!", gameid)
                possible = False
            elif (colour == 'blue' and int(number) > 14):
                print("Invalid game!", gameid)
                possible = False
    if (possible==True):
        sum_of_possible_games+=int(gameid)

print (sum_of_possible_games)