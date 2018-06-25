from random import randint
import json
#1 greift 2 an
def attacks2():
    with open('player2.json', 'r+') as player1_file:
        chardict = json.load(player1_file)
        damage = randint(1, 100)
        chardict['health'] -= damage
        player1_file.seek(0)
        player1_file.truncate()
        json.dump(chardict, player1_file,indent=2)
        return ('player1 attacks player2 and deals %s damage' % damage)

#2 greift 1 an
def attacks1():
    with open('player1.json', 'r+') as player2_file:
        chardict = json.load(player2_file)
        damage = randint(1, 100)
        chardict['health'] -= damage
        player2_file.seek(0)
        player2_file.truncate()
        json.dump(chardict, player2_file,indent=2)   
        return ('player2 attacks player1 and deals %s damage' % damage)