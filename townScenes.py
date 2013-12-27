import time
import sys

from gameMechanics import *

def takeBrotherInteraction(player):
    Jakob = Ally('Jakob', 'gunman')
    print ('You turn away from the door and walk towards your brother...\n'
            'As you approach, his head turns towards you and his eyes meet your gaze.\n'
            '\"Hey, ' + player.name + ' up and ready for the morning hunt, huh?\"'
            '\n\"Yeah, Jakob, you know the Saturday morning drill,\" you reply.\n'
            'Jakob lets out an uneasy chuckle. \"True, you\'ve been doing it for years...\"\n'
            'He pauses.\n\n')

    print ('Looking into his eyes, you can discern his look of expectation. Normally, you\'re too\n'
            'focused on your morning tasks to stop and chat. Approaching him like this is out of the ordinary.\n'
            'He must know what I\'m going to ask him, what he\'s been waiting for me to ask for a while now, you think..\n'
            '\n\"Well, speaking of the drill... I know I\'ve never taken you with me before but.. um..\"\n'
            '\"You want me to come along!\" He interupts you, overcome with excitement.\n'
            '\"Yeah, yeah that\'s exactly what I want.\"')
    
    print '\n\"But why?\"'
    print('Answer:\n'
            '1. Because I think you\'re ready to become a hunter, Jakob.\n'
            '2. I want to spend some time with you.\n'
            '3. It\'s someone else learns to support the family\n'
            '4. You need to learn to defend yourself...\n')
    choice = get_valid_choice("Which do you say?", ['1','2','3','4'])

    #if choice == '1':


    

class OpeningTownScene(Scene):

    #def __init__(self, player):
      #  self.player = player
        
    def run(self):
        print '\nCONTAGION'
        print '\n--------\n'
        time.sleep(3)
        print ('You awake to the sight of your hunting bow, resting on your bedside table,' 
               ' illuminated by a beam of light shining through the small slit in your window.\n'
               'You reach out and grab it, slinging it over your shoulder along with the quiver of '
               'arrows that laid on the ground beside it. \nIt\'s early morning, and the sun has just begun to rise. ')
        time.sleep(5)
        print('Now is the perfect time to head into the wilderness and begun the day\'s hunt.\n'
               '\nOn your way out of the door, you notice your younger brother, sitting'
               ' at the kitchen table, staring off into the distance. \nHe just turned 16. Old enough for'
               ' the draft now...')
        time.sleep(5)
        print '\nHesitation hits you as you\'re about to exit out the front door. \n'
        time.sleep(1)
        print '.'
        time.sleep(1)
        print '.'
        time.sleep(1)
        print '.'
        time.sleep(1)
        
        choice = get_valid_choice('Should you ask him to come along?', ['yes', 'no'])
        self.player.decisions['Opening_Take_Brother'] = choice
        
        if choice == 'yes':
     		takeBrotherInteraction(self.player)
     	else:
     		print ('\nYou look back at your brother. \nJust as you begin to move your eyes away,'
     			' his head turns and he meets your gaze. \nHis eyes seem weary, and you know that his mind is'
     			' weighed down by burdensome thoughts.\nFears.\nAnxieties.\nYou smile at him. \nHe nods and turns'
     			' his gaze back towards some unseen horizon.\nGiving him one last glance, you push open the door and'
     			' enter the brisk morning air. . .')

     	exit(1)


