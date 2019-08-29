class Mad_Lib:
    def __init__(self):
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

    def init(self):
        print("""
        Kevin is a very [adjective] [noun], he gets really [verb] people have 
        the same name as him. Sometimes, Kevin enjoys [indoor activity] with 
        his friend [noun].
        """)
        self.user_input = []
        self.user_input.insert(0, str(input("adjective: ")))
        self.user_input.insert(0, str(input("noun: ")))
        self.user_input.insert(0, str(input("verb: ")))
        self.user_input.insert(0, str(input("indoor activity: ")))
        self.user_input.insert(0, str(input("person: ")))
        self.create_mad_lib(self.user_input)

mad_lib = Mad_Lib()

mad_lib.init()