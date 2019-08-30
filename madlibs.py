class Mad_Lib:
     def __init__(self):
        self.user_input = []
        self.mad_lib = ['Kevin is a very', 'adjective', 'noun', ', he gets really', 'verb', 'when people have the same name as him. Sometimes during the weeked, Kevin enjoys', 'outdoor activity', 'outside with his friend', 'noun', '.', 'However, during the week, Kevin works for', 'noun', 'where he', 'adverb', 'verb', 'nine to five.' ]

    def insert_nouns(self, input):
        for word in self.mad_lid:
            if(word is 'noun'):
                word = random.choice(input)
                input.remove(word)

    def insert_verbs(self, input):
        for word in self.mad_lib:
            if(word is 'verb'):
                word = random.choice(input)
        

    def get_input(self):
        user_input = []
        adjective = str(input('adjective: '))
        while(adjective == ''):
            adjective = str(input('Invaled, a adjective is required: '))
        noun_1 = str(input('noun: '))
        while(noun_1 == ''):
            noun_1 = str(input('Invaled, a noun is required: '))
        verb = str(input('verb: '))
        while(verb == '' or validate_verb(verb) == False):
            verb = str(input('Invaled, a verb is required: '))
        outdoor_activity = str(input('outdoor activity: '))
        while(outdoor_activity == ''):
            outdoor_activity = str(input('Invaled, an activity is required: '))
        noun_2 = str(input('noun: '))
        while(noun_2 == ''):
            noun_2 = str(input('Invaled, a noun is required: '))

        user_input.insert(0, adjective) 
        user_input.insert(0, noun_1)
        user_input.insert(0, verb) 
        user_input.insert(0, outdoor_activity) 
        user_input.insert(0, noun_2)
        return user_input

    def init(self):
        self.create_mad_lib(self.get_input())
        
        

mad_lib = Mad_Lib()
mad_lib.init()


def test():
     print(f'''
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [outdoor activity] with 
        his friend [noun].
        ''')