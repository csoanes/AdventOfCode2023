import numpy as np
import regex as re
with open("day4data", 'r') as file:
    lines = [line.rstrip() for line in file]

print (lines)

total_points = 0

card_values={}

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
    card_values[int(cardId)]=len(common)

print(card_values)

card_amounts ={}

for card in card_values:
    card_amounts[card] = 1

for card in card_values:
    print (f'processing card {card}')
    if (card in card_amounts):
        number_of_this_card = card_amounts[card]
    else:
        number_of_this_card = 1

    prize_cards=card_values[card]
    print (f'card {card} wins {prize_cards} cards')
    print (range(card+1, card+1+prize_cards))
    for i in range(card+1,card+1+prize_cards):
        print (f'Adding {number_of_this_card} card(s) to {i}')
        if i not in card_amounts:
            card_amounts[i] = number_of_this_card
        else:
            current_card_amounts = card_amounts[i]
            current_card_amounts += number_of_this_card
            card_amounts.update({i: current_card_amounts})
    print(card_amounts)

print(sum(card_amounts.values()))

