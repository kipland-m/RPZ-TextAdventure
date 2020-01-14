#This file takes the values from item_db.txt and converts the data into separate lists

Item_DB = open('item_db.txt','r').read()

def ItemData():

    counter = 0

    Weapons = []
    Weapon_DMG = []

    Armor = []
    Armor_DEF = []

    Misc = []

    with open('item_db.txt', 'r') as file:      #Takes the info within item_db.txt and seperates weapons and weapon damage into seperate lists
        data = file.read().replace('\n', '')
        data = data.split(',')


        for element in data:    # Will need to expand this loop upon adding armor to text file



            if counter % 2 == 0:
                Weapons.append(element)

            elif counter % 2 != 0:
                Weapon_DMG.append(element)

            counter += 1


ItemData()


