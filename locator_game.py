"""
A simple program that can be used as a plugin for games to find your place on a virtual grid
Kipland Melton
"""


def Locator():


    x = 0
    y = 0


    if x == 0 and y == 0:
        player_loc = 'Spawn'

    elif x > 0 and y > 0:
        player_loc = 'Quadrant 1'

    elif x > 0 and y < 0:
        player_loc = 'Quadrant 2'

    elif x < 0 and y > 0:
        player_loc = 'Quadrant 3'

    elif x < 0 and y < 0:
        player_loc = 'Quadrant 4'



Locator()