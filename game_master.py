'''
Kipland Melton

     RPZ
the 300th text
adventure from
kipland melton

CHECK BOOK!
'''



import time
import locator_game
import random
import data_import
import intro_game

ItemData = data_import.Item_Import()
CharData = data_import.Char_Import()

GameInputs = [1,2,3,4]


def Player():

    player = {'name':'','class':'','race':'',
              'weapon':'','headpiece':'',
              'chestpiece':'','pants':'',
              'boots':'',}


def Enemy():

    enemy = {'race':'','class':''}


def MainGame():

    GameRunning = True


    print(CharData)





MainGame()
