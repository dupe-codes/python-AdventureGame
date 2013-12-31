import sys
import time

from gameMechanics import *
from townScenes import * 

class Map():
    #scenes = {'Opening_Town': openingTownScene(),}
    
    def __init__(self, start_scene, player):
        #self.scenes = {'Opening_Town': OpeningTownScene()}
        self.start_scene_name = start_scene
        self.player = player
        self.scenes = {'Opening_Scene': OpeningScene(player), 'Open_Town_Brother': OpenTownBrother(player)}
  #      print 'Map created with player ', player

    def opening_scene(self):
        return self.scenes.get(self.start_scene_name)

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)


class Engine():
    
    def __init__(self, map):
#        print 'Game Engine initialized with map ', map.start_scene_name
        self.scene_map = map

    def play(self):
        current_scene = self.scene_map.opening_scene()
 #       print 'Playing first scene: ', current_scene

        while True:
            print '\n--------'
            next_scene_name = current_scene.run()
            print 'Next scene: ', next_scene_name
            raw_input("Pause")
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "Map gives new scene: ", current_scene 

    def test(self):
        test_scene = self.scene_map.next_scene("Opening_Scene")
        test_scene.run()



