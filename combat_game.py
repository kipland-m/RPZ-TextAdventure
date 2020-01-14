#Combat Module for RPZ, contains loop for combat


import random
import time


def InCombat(player_hp): #This function defines the W-I-P combat loop for the game, very much a prototype at this stage


    enemy_HP = 100

    InCombat = True

    while InCombat == True:

        print('\nHP:',player_hp)
        Combat_Input = int(input('Press 1 to attack: '))


        if Combat_Input == 1:
            damage = random.randrange(15,25)
            enemy_damage = random.randrange(5,20)
            crit_chance = random.randrange(1,4)

            if damage > 20:
                damage = damage+15
                print('\nCRITICAL STRIKE!',damage,'DAMAGE TO ENEMY!')

            if enemy_damage > 10:
                enemy_damage = enemy_damage+10
                player_hp = player_hp-enemy_damage
                print('\nCRUSHING BLOW!',enemy_damage,'DAMAGE TO PLAYER!')

            else:
                player_hp = player_hp-enemy_damage

            enemy_HP = enemy_HP - damage

            print('\nYou hit the monster for', damage, 'leaving it with', enemy_HP, 'health')
            print('The monster hit you for',enemy_damage,'leaving you with',player_hp,'health')

        if enemy_HP <= 0:

            print('\n------YOU DEFEATED------\n')

            game_restart = int(input('Would you like to fight again?\n1. Yes\n2. No\nChoice: '))

            if game_restart == 1:
                InCombat = True
                player_hp = 100
                enemy_HP = 100

            else:
                print("\nBYE!")
                InCombat = False

InCombat(100) 