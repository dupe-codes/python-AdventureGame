
class Scene():

	def __init__(self, player):
		self.player = player

	def run(self):
		pass

def get_valid_choice(question, options):
    while True:
        print '\n', question
        user_input = raw_input('>')
        if user_input.lower() in options: return user_input.lower()
        print 'This is an invalid choice. Please try again.'
        
        
    
