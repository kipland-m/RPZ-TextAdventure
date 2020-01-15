#Function to run the intro for the game

import ui_elements

char_sheet = open('char_sheet.txt','a') #Opens the character sheet to which all character creation info will be saved to


def Char_Save(type,info): #Type determines what line the info will be saved to in char_sheet.txt

    # Each of the numbers corresponds to the line to which that data will be saved in char_sheet.txt

    if type == 1:                   # 1 = Name  
        char_sheet.write(info)
        char_sheet.write('\n')    
    elif type == 2:                 # 2 = Race
        char_sheet.write(info)
        char_sheet.write('\n')
    elif type == 3:                 # 3 = Class
        char_sheet.write(info)
        char_sheet.write('\n')
    elif type == 4:                 # 4 = Strength Stat
        char_sheet.write(info)
        char_sheet.write('\n')
    elif type == 5:                 # 5 = Stamina Stat
        char_sheet.write(info)
        char_sheet.write('\n')
    elif type == 6:                 # 6 = Agility Stat
        char_sheet.write(info)
        char_sheet.write('\n')
    elif type == 7:                 # 7 = Intellect Stat
        char_sheet.write(info)
        char_sheet.write('\n')

    
def StartingZone(p_name,p_race,p_class): # Function to run the start of the game
        
    print('''
    You are''',p_name,'''the mighty''',p_race,p_class+".")

    print('''
    You awaken inside of a dilapitated clinic with no recollection of how you arrived here with no soul in sight.
    What would you like to do?
    1.) Walk out the front door.
    2.) Search the cabinent.
    3.) Enter the back room.''')

    p_input = input('''
    Choice: ''')




def NewGame(): #This function runs the character creation for the game 

    print('''
    Welcome to RPZ!
    Everything is a WIP
    (please add world building exposition here thanks!)''')

    print('''
    Enter your name.''')

    ng_name = input('''
    Name: ''').title()

    Char_Save(1,ng_name)

    print('''
    Please choose your race.\n
    1.) Ioldnir | A noble sub-race of humans with thicker skin and stronger bones, but less intellect.
    2.) Faerith | An elven sub-race that is highly skilled in arcane arts, though distinct tribes are known for other professions.
    3.) Thorogg | An ogre like race that are incapable of things other than smashing their foes into bits.
    4.) Uldman  | An impressionable sub-race of humans that are not exceptionally well at anything.''')

    race_choice = int(input('''
    Choice: '''))


    if race_choice == 1:
        ng_race = 'Ioldnir'
    elif race_choice == 2:
        ng_race = 'Faerith'
    elif race_choice == 3:
        ng_race = 'Thorogg'
    elif race_choice == 4:
        ng_race = 'Uldman'

    Char_Save(2,ng_race)

    print('''
    Please choose your class.\n
    1.) Warrior | A melee dominant class that specializes in 2 handed weapons. 
    2.) Wizard  | A ranged magic class that specializes in wands and staves.
    3.) Thief   | A melee class that specializes in one handed weapons.
    4.) Ranger  | A ranged class that specializes in bows and crossbows.''')

    class_choice = int(input('''
    Choice: '''))

    if class_choice == 1:
        ng_class = 'Warrior'
    elif class_choice == 2:
        ng_class = 'Wizard'
    elif class_choice == 3:
        ng_class = 'Thief'
    elif class_choice == 4:
        ng_class = 'Ranger'

    Char_Save(3,ng_class)

    # Need to write code to append stats corresponding to race/class choice to char_sheet.txt

    StartingZone(ng_name,ng_race,ng_class)


def StartScreen(): #This function defines the main menu for the game 

    print('''
    ######  ######  ####### 
    #     # #     #      #  
    #     # #     #     #   
    ######  ######     #    
    #   #   #         #     
    #    #  #        #      
    #     # #       ####### ''')
    print('''
    Welcome to RPZ
    1. Start New Game
    2. Load Game (Yet to be implemented).
    3. Settings (Yet to be implemented)''')

    ss_input = int(input("""
    Choice: """))       

    if ss_input == 1:
        NewGame()

StartScreen()

