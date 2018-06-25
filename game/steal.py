import json
from random import randint

def steals1():
    with open('player1.json', 'r+') as player1_file:
        char1 = json.load(player1_file)
        len_char1 = len(char1['items'])
        rand_item = randint(0,len_char1-1)
        item_stolen = char1['items'][rand_item]
        char1['items'].pop(rand_item)
        json.dump(char1, player1_file)
        player1_file.close()
    with open('player2.json', 'r+') as player2_file:
        char2 = json.load(player2_file)
        char2['items'].append(item_stolen)
        json.dump(char2, player2_file)
        player2_file.close()
    return ('player2 stole %s from player1' % item_stolen)

def steals2():
    with open('player2.json', 'r+') as player2_file:
        char2 = json.load(player2_file)
        len_char2 = len(char2['items'])
        rand_item = randint(0,len_char2-1)
        item_stolen = char2['items'][rand_item]
        char2['items'].pop(rand_item)
        json.dump(char2, player2_file, indent=2)
        player2_file.close()
    with open('player1.json', 'r+') as player1_file:
        char1 = json.load(player1_file)
        char1['items'].append(item_stolen)
        json.dump(char1, player1_file, indent=2)
        player1_file.close()
    return ('player1 stole %s from player2' % item_stolen)