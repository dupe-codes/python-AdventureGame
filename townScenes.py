import time
import sys

from gameMechanics import *
from Characters import *

def takeBrotherInteraction(player):
    Jakob = Ally('Jakob', 'gunman', 95, 40)
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
            '1. It doesn\'t matter why.\n' # - opinion
            '2. Because you\'re ready to become a hunter of course!\n' # + morale
            '3. It\'s time someone else learns to support the family\n' # neutral 
            '4. You need to learn to defend yourself...\n') # - morale
    choice = get_valid_choice("Which do you say?", ['1','2','3','4'])

    if choice == '1':
        print('\nNot expecting you to deflect his question, Jakob looks taken aback.\n'
                'You can tell your answer hurt him.\n')
        Jakob.updateOpinion(-5)
        print Jakob.playerOpinion
        print('\n\"Oh.. uh.. alright. Well I\'m ready when you are!\"')
    elif choice == '2':
        print('\nYou see Jakob\'s eyes light up as your words reach his ears.\n'
                'You know your words gave him just the morale boost he needed.\n')
        Jakob.updateMorale(5)
        print Jakob.morale
        print('\n\"I\'ve been waiting for you to say that for so long! Let\'s do this!\"')
    elif choice == '3':
        print('\nJakob nods in acceptance of your straightforward and level answer.\n'
                'You can tell he accepts it as rational.')
        print('\n\"Makes sense. Well, let\'s go then.\"')
    else:
        print('\nJakob\'s eyes dart to his feet as your words sink in.\n'
                'You sense that heavy weight on his shoulders growing.')
        Jakob.updateMorale(-5)
        print Jakob.morale
        print('\n\"Yeah.. yeah, I suppose you\'re right. Let\'s go, then.\"')

    print('\n\nJakob lifts himself up from his chair and starts to walk towards the front door...\n'
            '\"Wait, you\'re forgeting something.\" You call to him, just as he reaches the door.\n'
            'He stops. \"What?\"\n'
            '\"Planning on hunting with just your fists?\"'
            '\n\"Oh.. no, my mistake.\" He chuckles. \"Okay, well what weapon should I bring?\"')
    print('\nYou glance over at the shelf mounted on the wall beside you. On it lies your brother\'s weapons.\n'
            'An old rifle, worn from use, passed down to him from your father, before he died.. \n'
            'A shortbow, covered with a thin layer of dust.\n'
            'Around town, your brother is known as the neighborhood marksman - with a rifle in his hands, that is. He\'s'
            'a sure shot with the rifle, but inexperienced with a bow. But a bow is more suited for the type of hunting you do.\n'
            'The dust on that bow has touched it more than my brother ever has, you pause and think.\n'
            '\nA rifle is noisy and may drive away prey, but your brother is more experienced with it.')
    print('\nChoices:\n'
            '1. The rifle\n'
            '2. The bow\n')
    choice = get_valid_choice('Which should he bring?', ['1', '2'])
    
    if choice == '1':
        print ('\"Grab your rifle, Jakob. I want you to bring your A-game.\"\n'
                'Jakob walks over to the shelf and grabs his rifle, along with one case of ammo. He slings the rifle over'
                '\nhis shoulder, and throws the ammunition into his bag.')
        Jakob.addToInventory('rifle')
        Jakob.addToInventory('ammo')
        print Jakob.inventory 
        Jakob.weapon = 'rifle'
        player.decisions['Brother_Weapon'] = 'rifle'
    else:
        print ('\"Grab the bow. I don\'t want you scaring off any game with a loud gunshot.\"\n'
                'Jakob moves over to the shelf and grabs the bow, slinging it over his shoulder.\n'
                'He then reaches into a nearby closet and pulls out a sheath of arrows.')
        Jakob.addToInventory('bow')
        Jakob.addToInventory('arrows')
        print Jakob.inventory
        Jakob.weapon = 'bow'
        player.decisions['Brother_Weapon'] = 'bow'

    print player.decisions

    print('\nJakob turns back to you. \"Okay, NOW I\'m ready!\"'
            '\nYou look at him and smile. \"Yeah, you are. Let\'s go.\"'
            '\nYou move towards the door and swing it open. You step out and glance back into the doorway\n'
            'Jakob looks at you and smiles, and steps out after you, into the cold morning air. . .')

    player.addToParty(Jakob)
    print player.partymembers


class OpenTownBrother(Scene):

    def __init__(self, player):
        self.player = player

    def run(self):
        print '\n---------------------\n'
        print('\nYou set a course for the entrance to the woods, walking at a quick pace. \n'
                'Your brother lags behind you, struggling to keep up.')


class OpeningScene(Scene):

    def __init__(self, player):
        self.player = player
        
    def run(self):
        print '\nCONTAGION'
        print '\n--------\n'
        #time.sleep(3)
        print ('You awake to the sight of your hunting bow, resting on your bedside table,' 
               ' illuminated by a beam of light shining through the small slit in your window.\n'
               'You reach out and grab it, slinging it over your shoulder along with the quiver of '
               'arrows that laid on the ground beside it. \nIt\'s early morning, and the sun has just begun to rise. ')
       # time.sleep(5)
        print('Now is the perfect time to head into the wilderness and begun the day\'s hunt.\n'
               '\nOn your way out of the door, you notice your younger brother, sitting'
               ' at the kitchen table, staring off into the distance. \nYou sense an unseen weight on him. He just turned 16. Old enough for'
               ' the draft now...')
       # time.sleep(5)
        print '\nHesitation hits you as you\'re about to exit out the front door. \n'
        #time.sleep(1)
        print '.'
        #time.sleep(1)
        print '.'
        #time.sleep(1)
        print '.'
        #time.sleep(1)
        
        choice = get_valid_choice('Should you ask him to come along?', ['yes', 'no'])
        self.player.decisions['Opening_Take_Brother'] = choice
        
        if choice == 'yes':
            takeBrotherInteraction(self.player)
            return 'Open_Town_Brother'
        else:
            print ('\nYou look back at your brother. \nJust as you begin to move your eyes away,'
     			' his head turns and he meets your gaze. \nHis eyes seem weary, and you know that his mind is'
     			' weighed down by burdensome thoughts.\nFears.\nAnxieties.\nYou smile at him. \nHe nods and turns'
     			' his gaze back towards some unseen horizon.\nGiving him one last glance, you push open the door and'
     			' enter the brisk morning air. . .')
            return 'Open_Town_Alone'




