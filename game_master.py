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
import item_import
import intro_game

ItemData = item_import.ItemData()


def Player():

    player = {'name':'','class':'','race':'',
              'weapon':'','headpiece':'',
              'chestpiece':'','pants':'',
              'boots':'',}


def Enemy():

    enemy = {'race':'','class':''}


def MainGame():

    GameRunning = True

    while GameRunning == True:
        intro_game.StartScreen()


MainGame()
