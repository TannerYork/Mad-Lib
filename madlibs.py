class Mad_Lib:
    def __init__(self):
        self.user_input = []
        self.mad_lib = ["Kevin is a very ", None, None, ", he gets really ", None, "when people have the same name as him. Sometimes, Kevin enjoys ", None, "inside with his friend ", None, "."]

    def create_mad_lib(self, input):
        if(len(input) == 5):
            for input_i, word in reversed(list(enumerate(input))):
                for mad_i, value in enumerate(self.mad_lib):
                    if(value is None):
                        self.mad_lib[mad_i] = word
                        input.pop(input_i)
                        break
                continue
            print('')
            print(''.join(self.mad_lib))
        else:
            print("invalid number of inputs")
    
    def get_input(self):
        user_input = []
        adjective = str(input("adjective: "))
        while(adjective == ''):
            adjective = str(input("Invaled, a adjective is required: "))
        noun_1 = str(input("noun: "))
        while(noun_1 == ''):
            noun_1 = str(input("Invaled, a noun is required: "))
        verb = str(input("verb: "))
        while(verb == ''):
            verb = str(input("Invaled, a verb is required: "))
        indoor_activity = str(input("indoor activity: "))
        while(indoor_activity == ''):
            indoor_activity = str(input("Invaled, an activity is required: "))
        noun_2 = str(input("noun: "))
        while(noun_2 == ''):
            noun_2 = str(input("Invaled, a noun is required: "))

        user_input.insert(0, adjective) 
        user_input.insert(0, noun_1)
        user_input.insert(0, verb) 
        user_input.insert(0, indoor_activity) 
        user_input.insert(0, noun_2)
        return user_input

    def init(self):
        self.create_mad_lib(self.get_input())
        
        

mad_lib = Mad_Lib()
mad_lib.init()


def test():
     print(f"""
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [indoor activity] with 
        his friend [noun].
        """)