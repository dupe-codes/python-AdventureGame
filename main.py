#!/usr/bin/env python

import sys

from Characters import *
from gameEngine import *


def testAllyCreation():
    test = Ally('Phil', 'archer')
    print test.getInfo()

    test2 = Ally('Bob', 'gunman')
    print test2.getInfo()
    
def test():
    print 'Testing character creation..'
    testPlayer = Player('Edward')
    print testPlayer.name
    
    g_map = Map('Opening_Town', testPlayer)
    g_engine = Engine(g_map)
    g_engine.play()

def player_creation():
    print ('--------\n'
           'Welcome to the game of CONTAGION!\n'
           '--------\n'
           'Before you dive into your adventure, you must create your character. . .'
           '\nFirst, what is your name?')
    player_name = raw_input('>')
    return Player(player_name)

def openingGameMessage():
    print ('Game Start')
    
if __name__ == '__main__':
    #test()
    #testAllyCreation()
    openingGameMessage()
    player = player_creation()
    raw_input('Great! You\'re all set! Press Enter to begin!')
    
    g_map = Map('Opening_Town', player)
    g_engine = Engine(g_map)
    g_engine.play()

