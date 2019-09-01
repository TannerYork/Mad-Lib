import random
import re

class Mad_Lib:
    def __init__(self, mad_lib):
        self.mad_lib = mad_lib
        
    # Take any text inclosed in [] and inserts it into the inputs array  
    def user_inputs(self):
        inputs = re.findall('\[([a-z]([a-z]|\s)+)\]', self.mad_lib)
        for index, item in enumerate(inputs): inputs[index] = item[0]
        user_inputs = {}
        for item in inputs: user_inputs[item] = input(f"{item}: ")
        return user_inputs

    # Subbsitute bracket inclosed text with user input
    def create(self):
        for key, value in self.user_inputs().items():
            self.mad_lib = re.sub(f'\[{key}\]', value, self.mad_lib)

    def print(self):
        print(self.mad_lib)

global_mad_lib = '''
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [outdoor activity] with 
        his friend [noun].
        '''
mad_lib = Mad_Lib(global_mad_lib)
mad_lib.create()
mad_lib.print()

def test():
     print(f'''
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [outdoor activity] with 
        his friend [noun].
        ''')