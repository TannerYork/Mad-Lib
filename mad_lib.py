def create_mad_lib(adjective, noun, verb, indoor_activity, person, outdoor_activity):
    return f""" Kevin is a very {adjective} {noun}, he gets really {verb} when people have the same name as him. 
 Sometimes, Kevin enjoys {indoor_activity} inside with his friend {person}. When Kevin and {person} 
 can't {indoor_activity} inside they choose to {outdoor_activity} outside instead. """

print(""" Kevin is a very {adjective} {noun}, he gets really {verb} when people have the same name as him. 
 Sometimes, Kevin enjoys {indoor activity} inside with his friend {person}. When Kevin and {person} can't 
 {indoor_activity} inside they choose to {outdoor activity} outside instead.  """)

adjective = str(input("adjective: "))
noun = str(input("noun: "))
verb = str(input("verb: "))
indoor_activity = str(input("indoor activity: "))
person = str(input("person: "))
outdoor_activity = str(input("outdoor activity: "))

print(create_mad_lib(adjective, noun, verb, indoor_activity, person, outdoor_activity))