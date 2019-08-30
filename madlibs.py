import random

class Mad_Lib:
    def __init__(self, mad_lib):
        self.user_input = {
            "name": None,
            "nouns": [],
            "verbs": [],
            "adjectives": [],
            "adverbs": []
        }
        self.mad_lib = mad_lib

    def get_input(self, input_type):
        for word in self.mad_lib:
            if(word == input_type):
                inputs = [input(f'{input_type}: ')]
                while(inputs[0] is ''):
                    inputs[0] = input(f'Invaled, {input_type} is required: ')
                self.user_input[f"{input_type}s"].append(inputs[0])
    
    def get_name_input(self):
        name = input('Name: ')
        while(name is ''):
            name = input('Invaled, a name is required: ')
    
    def get_user_input(self):
        self.get_name_input()
        self.get_input('noun')
        self.get_input('verb')
        self.get_input('adjective')
        self.get_input('adverb')

    def insert_input(self, list_type):
        for i, word in enumerate(self.mad_lib):
            if(word == list_type):
                random_word = random.choice(self.user_input[f"{list_type}s"])
                self.mad_lib[i] = random_word
                self.user_input[f"{list_type}s"].remove(random_word)

    def insert_name_input(self):
        for word in self.mad_lib:
            if(word == 'name'):
                word = self.user_input["name"]

    def create(self):
        self.insert_name_input()
        self.insert_input('noun')
        self.insert_input('verb')
        self.insert_input('adjective')
        self.insert_input('adverb')

    def init(self):
        self.get_user_input()
        self.create()
        print("".join(self.mad_lib))
        
        
        
jack_and_bean = ['Once upon a time there lived a ', 'adjective', ' ', 'noun', ' and her ', 'noun',' ', 'name', '. One day, ', 'name', "'s ", 'noun', ' told him to ', 'verb', ' their only ', 'noun', '.', ' name', ' went to the ', 'noun', ' and on the way he met a man who wanted to buy his ', 'noun', '. Jack asked, ', '"What will you give me for my ', 'noun', '? The man answered, “I will ', 'verb', ' you five ', 'adjective', ' ', 'noun', '!” ', 'name', ' took the ', 'adverb',' ', 'verb',' ', 'noun', ' and gave the man the ', 'noun', '. But when he', 'verb', ' ', 'place', ' ', 'name', "'s ", 'noun', ' was very ', 'verb', '. She said, “You ', 'adjective', '! He took away your ', 'noun', ' and gave you some ', 'noun', '!” She ', 'verb', ' the ', 'noun', ' out of the ', 'noun', '. ', 'name', ' was very ', 'adjective', ' and went to ', 'verb', ' without ', 'noun', '.']
kevin = ['Kevin is a very ', 'adjective', ' ', 'noun', ' he gets really ', 'verb', ' when people have the same name as him. Sometimes, Kevin enjoys ', 'verb', ' with his friend ', 'noun', '.']


story_types = [str(input('What type of story would your like, long or short? '))]

while(story_types[0] not 'long' or story_types[0] not 'short'):
    print(story_types[0])
    story_types[0] = str(input('The only options are long or short: '))

if(story_types[0] == 'long'):
    mad_lib = Mad_Lib(jack_and_bean)
    mad_lib.init()

else:
    kevin_mad_lib = Mad_Lib(kevin)
    kevin_mad_lib.init()


def test():
     print(f'''
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [outdoor activity] with 
        his friend [noun].
        ''')
