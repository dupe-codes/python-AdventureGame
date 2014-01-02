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
        
        Jakob = self.player.getFromParty('Jakob')

        print('\nYou set a course for the entrance to the woods, walking at a quick pace. \n'
                'Your house fades into the distance behind you, as you work'
                ' your way down the hill it stands on.\n'
                'You walk on an old, faint dirt path, beaten into the earth by the footsteps of men, horses,'
                ' and the pressure of animal carcasses dragged behind them. \n'
                'Only your family has ever lived up this hill, and so the path is one created by the toils of'
                ' you and your loved ones.\n\n'
                'Your brother lags behind you, struggling to keep up.'
                '\nYou can hear him call out for you to slow down.\n')
        choice = get_valid_choice('Do you let him catch up?', ['yes', 'no', 'y', 'n'])

        if choice == 'yes' or choice == 'y':
            print('\nYou slow down your pace just enough to allow your brother to catch up.\n'
                    'When he makes it to your side, he turns and nods his head in thanks.\n'
                    'You nod back, knowing your brother appreciates the gesture.')
            Jakob.updateOpinion(5)
            self.player.decisions['Brother_Catchup'] = 'yes'
            #print Jakob.playerOpinion

        else:
            print('\nYou ignore your brother\'s calls, and continue your quick pace.\n'
                    'Taking a moment to look back over your shoulder, you see your brother several '
                    'yards behind you, shaking his head in anger and frustration.\n')
            Jakob.updateOpinion(-5)
            self.player.decisions['Brother_Catchup'] = 'no'
            #print Jakob.playerOpinion

        print('\nAfter walking for several more minutes, you reach the main part of town.\n'
                'The small town you live in is situated around a rectangular town-center. Rundown buildings line'
                ' the sides of the townsquare, each ragged with damage. Many have whole sections of their' 
                ' walls blown out, with sheets of metal haphazardly placed to repair the gaping holes.\n'
                'Hollow attempts to shelter the building\'s inhabitants from the elements. The cold and rain finds its way'
                ' in no matter what.\n'
                'Entering the townsquare, the armory, post office, and sheriff\'s building lie to your left.\n'
                'In front of you stands the Mayor\'s house and office. Every other building in the'
                ' square houses some sort of shop, owned by the \"wealthier\" town merchants.')

        print('\n\nYour path to the entrance of the woods continues on the other side of the square, past the Mayor\'s house.'
                'Walking through the square, you see little signs of the day beginning to start. A few shopkeepers are '
                'out and about, preparing for a long day of trading. You see the town sheriff sitting outside '
                'the sheriff\'s building, brushing his horse\'s mane.\n')
        print ('\nAnd out of the corner of your eye, you see her approaching. She\'s about your age and only '
                ' a few inches shorter. Her dirty blond hair falls in waves down to her shoulders.\n'
                'And as you turn to face her, you catch her deep, auburn eyes locked right onto you.')

        Cinder = Ally('Cinder', 'rogue', 80, 70)

        print('\n\"Hey ' + self.player.name + ', in a hurry?\"\n'
                'Her voice is hoarse, but holds a sweet undertone.\n')
        print('\nChoices:\n'
                '1. Yeah, I am. Going hunting.\n'
                '2. No, I can chat for a bit.\n'
                '3. None of your business\n')
        
        choice = get_valid_choice('Which do you say?', ['1', '2', '3'])

        if choice == '1':
            print('\n\"Oh I figured, that\'s all you ever do really, go hunting.\"')
        elif choice == '2':
            print '\nFor a brief moment, her eyes light up. You can tell your answer pleased her.\n'
            print('\"Really? Oh, great! I mean, I figured you\'re busy heading out to hunt.\"\n')
            Cinder.updateOpinion(5)
        else: 
            print ('\nYou see a scowl break out on her face, one that she quickly conceals.\n'
                    'Your answer obviously irritated her.\n')
            print('\"Feeling snippy today, huh? I already know you\'re going hunting.\"')
            Cinder.updateOpinion(-5)

        with_brother = self.player.decisions['Brother_Catchup']
        if with_brother == 'yes':
            print('\nShe glances over at your brother, standing silent by your side.\n'
                    '\"Well, good morning to you too, Jakob.\"\n'
                    '\"Morning Cinder,\" Jakob grunts out in reply.')
        else:
            print('\nThe sound of panting arrives beside you, and you turn to see that your '
                    'brother has finally caught up to you.\n'
                    '\"Thanks for waiting up for me,\" he sarcastically mutters.\n'
                    'After a few seconds of catching his breath, he notices the girl standing before you.\n'
                    '\"Oh hey, Cinder.\"')







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




