#!/usr/bin/env python
import time

from actors import *


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------------------------------------')
    print('                           WIZARD                             ')
    print('--------------------------------------------------------------')
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Panther', 12),
        Creature('Skeleton', 3),
        Dragon('Dragon', 50, 15, True),
        Wizard('Evil Wizard', 300),
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        # Win if creatures defeated
        if not creatures:
            print('You win!')
            break

        # Randomly select and introduce creature
        creature = random.choice(creatures)
        print()
        print('You are a wizard of level {}. A {} of level {} has appeared from a dark and foggy forest...'.format(
            hero.level, creature.name, creature.level)
        )

        # Select hero action
        cmd = input('[a]ttack, [r]un away, or [l]ook around: ')
        if cmd == 'a':
            if attack(hero, creature):
                print('The wizard triumphed over {}'.format(creature.name))
                hero.level += creature.level
                creatures.remove(creature)
            else:
                print('The wizard is defeated...')
                rest()
        elif cmd == 'r':
            print('The wizard is unsure of his power and flees...')
        elif cmd == 'l':
            print('The wizard takes in the surroundings and sees:')
            for c in creatures:
                print("  * A {} of level {}".format(c.name, c.level))
        else:
            print('Unrecognized action, goodbye.')
            break


def attack(hero, creature):
    print('The wizard {} attacks {}!'.format(hero.name, creature.name))
    hero_roll = hero.roll_die()
    creature_roll = creature.roll_die()
    print('  * {} rolls {}...'.format(hero.name, hero_roll))
    print('  * {} rolls {}...'.format(creature.name, creature_roll))
    return hero_roll >= creature_roll


def rest():
    print('The wizards hides, taking time to recover...')
    time.sleep(5)
    print('The wizard returns revitalized!')


if __name__ == '__main__':
    main()
