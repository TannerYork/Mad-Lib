from termcolor import colored
import random
import re

class Mad_Lib:
    def __init__(self, mad_lib):
        self.mad_lib = mad_lib
        self.user_inputs = {}
        
    # Check if user input is not blank and the correct pos, if avaliable.
    def is_valid(self, pos, user_input):
        if type(user_input) == str:
            if user_input == '' or re.match('\s+', user_input):
                return False
            else: 
                return True

    # Take any text inclosed in [] and inserts it into the inputs array  
    def get_inputs(self):
        # Get the inputs from the mad lib and set each input to it's pos tupal value
        tuple_inputs = re.findall('\[([a-z]([a-z]|\s)+)\]', self.mad_lib)
        for index, mad_lib_tuple in enumerate(tuple_inputs): tuple_inputs[index] = mad_lib_tuple[0]
        # Get proper pos user input, if input is a pos, for each input
        for mad_lib_input in tuple_inputs: 
            user_input = input(f'{mad_lib_input}: ') 
            while not self.is_valid(mad_lib_input, user_input):
                user_input = input(f'Invaled, input is not a {mad_lib_input}: ')
            if (mad_lib_input not in self.user_inputs): 
                self.user_inputs[mad_lib_input] = [colored(user_input, 'green')] 
            else:
                self.user_inputs[mad_lib_input].append(colored(user_input, 'green'))

    # Subbsitute bracket inclosed text with user input
    def create(self):
        self.get_inputs()
        for key in self.user_inputs.keys():
            # Shuffle the user input for each pos and insert them into mad lib
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
        Once upon a time there was a hare who, [verb] how he could [action verb] [comparative adjective] 
        than anyone else. He always would be [word that ends in ing] tortoise for its [adjective]. Then 
        one day, the [adjective] tortoise [verb] back: “Who do you think you are? There’s no denying 
        you’re [adjective], but even you can be [adjective]!” The hare [verb] with [noun]. “[verb] 
        in a [competition]? By whom? Not you, surely! I bet there’s nobody in the [noun] that can win 
        against me, I’m so [adjective]. Now, why don’t you [verb] off?”
        '''

mad_lib = Mad_Lib(tortoise_and_the_hair)
mad_lib.create()
mad_lib.print()