import random
import re

class Mad_Lib:
    def __init__(self, mad_lib):
        self.mad_lib = mad_lib
        self.user_inputs = {}
        
    # Take any text inclosed in [] and inserts it into the inputs array  
    def get_inputs(self):
        inputs = re.findall('\[([a-z]([a-z]|\s)+)\]', self.mad_lib)
        for index, item in enumerate(inputs): inputs[index] = item[0]
        for item in inputs: 
            user_input = input(f'{item}: ') 
            while user_input == '' or re.match('\s+', user_input):
                user_input = input(f'Invaled, {item} is required: ')
            if (item not in self.user_inputs): 
                self.user_inputs[item] = [user_input] 
            else:
                self.user_inputs[item].append(user_input)

    # Subbsitute bracket inclosed text with user input
    def create(self):
        self.get_inputs()
        for key in self.user_inputs.keys():
            shuffled_list = random.sample(self.user_inputs[key], len(self.user_inputs[key]))
            for index, word in enumerate(reversed(list(shuffled_list))):
                self.mad_lib = re.sub(f'\[{key}\]', word, self.mad_lib, 1)

    def print(self):
        print(self.mad_lib)

kevin_mad_lib = '''
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [outdoor activity] with 
        his friend [noun].
        '''
tortoise_and_the_hair = '''
        Once upon a time there was a hare who, [verb] how he could [verb] [adverb] than anyone else.
        He always would be [word that ends in ing] tortoise for its [adjective]. Then one day, the 
        [adjective] tortoise [verb] back: “Who do you think you are? There’s no denying you’re 
        [adjective], but even you can be [adjective]!” The hare [verb] with [noun]. “[action verb] in a 
        [competition]? By whom? Not you, surely! I bet there’s nobody in the [place] that can win against 
        me, I’m so [adjective]. Now, why don’t you [verb]?”
        '''
mad_lib = Mad_Lib(tortoise_and_the_hair)
mad_lib.create()
mad_lib.print()

def test():
     print(f'''
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [outdoor activity] with 
        his friend [noun].
        ''')