class Mad_Lib:
    def __init__(self):
        self.user_input = []
        self.mad_lib = ["Kevin is a very ", None, None, ", he gets really ", None, "when people have the same name as him. Sometimes, Kevin enjoys ", None, "inside with his friend ", None, "."]

    def create_mad_lib(self):
        if(len(self.user_input) == 5):
            for input_i, word in reversed(list(enumerate(self.user_input))):
                for mad_i, value in enumerate(self.mad_lib):
                    if(value is None):
                        self.mad_lib[mad_i] = word
                        self.user_input.pop(input_i)
                        break
                continue
            print('')
            print(''.join(self.mad_lib))
        else:
            print("invalid number of inputs")
    
    def getInput(self):
        adjective = str(input("adjective: "))
        noun = str(input("noun: "))
        verb = str(input("verb: "))
        indoor_activity = str(input("indoor activity: "))
        person = str(input("person: "))

        (self.user_input.insert(0, adjective)) if adjective != '' else None
        (self.user_input.insert(0, noun)) if noun != '' else None
        (self.user_input.insert(0, verb)) if verb != '' else None
        (self.user_input.insert(0, indoor_activity)) if indoor_activity != '' else None
        (self.user_input.insert(0, person)) if person != '' else None

    def init(self):
        print("""
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [indoor activity] with 
        his friend [noun].
        """)
        self.getInput()
        self.create_mad_lib()
        
        

mad_lib = Mad_Lib()

mad_lib.init()