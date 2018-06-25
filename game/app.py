from flask import Flask, abort, redirect, url_for
from random import randint
import os
import json

app = Flask(__name__)


@app.route('/status/<player>')
def check_status_player(player):
    return open(player + '.json', 'r').read()

@app.route('/attack/<player1>/<player2>')
def attack(player1, player2):
    with open(player2 + '.json', 'r+') as player2_file:
        chardict = json.load(player2_file)
        maximum = chardict['health']
        damage = randint(1, maximum)
        chardict['health'] -= damage
        player2_file.seek(0)
        player2_file.truncate()
        json.dump(chardict, player2_file,indent=2)
        player2_file.close()
        return (player1 + ' attacks ' + player2 + ' and deals ' + damage +' damage.')

@app.route('/steal/<player2>/<player1>')
def steal(player1, player2):
    with open(player1 + '.json', 'r+') as player1_file:
        char1 = json.load(player1_file)
        len_char1 = len(char1['items'])
        rand_item = randint(0,len_char1-1)
        item_stolen = char1['items'][rand_item]
        char1['items'].pop(rand_item)
        player1_file.seek(0)
        player1_file.truncate()
        json.dump(char1, player1_file)
        player1_file.close()
    with open(player2 + '.json', 'r+') as player2_file:
        char2 = json.load(player2_file)
        char2['items'].append(item_stolen)
        player2_file.seek(0)
        player2_file.truncate()
        json.dump(char2, player2_file)
        player2_file.close()
    return (player2 + ' stole ' + item_stolen + ' from ' + player1)

@app.route('/addplayer/<name>/<age>/<health>')
def addplayer(name, age, health):
    with open('newplayer.json', 'x') as newplayer:
        default_list = {"name": name, "age": int(age), "health": int(health), "items": []}
        rnumber = randint(1,3)
        if rnumber == 1:
            default_list['items'].append('Apple')
        elif rnumber == 2:
            default_list['items'].append('Apple')
            default_list['items'].append('Knife')
        else:
            default_list['items'].append('Apple')
            default_list['items'].append('Knife')
            default_list['items'].append('Bow')
        json.dump(default_list, newplayer, indent=2)
        newplayer.close()
        os.rename('newplayer.json', '%s.json' % name)
    return open(name + '.json', 'r').read()

        

