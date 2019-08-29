def create_mad_lib(input):
    return f""" Kevin is a very {input["adjective"]} {input["noun"]}, he gets really {input["verb"]} when people have the same name as him. 
 Sometimes, Kevin enjoys {input["indoor_activity"]} inside with his friend {input["person"]}. When Kevin and {input["person"]} 
 can't {input["indoor_activity"]} inside they choose to {input["outdoor_activity"]} outside instead. """

print(""" Kevin is a very {adjective} {noun}, he gets really {verb} when people have the same name as him. 
 Sometimes, Kevin enjoys {indoor activity} inside with his friend {person}. When Kevin and {person} can't 
 {indoor_activity} inside they choose to {outdoor activity} outside instead.  """)

adjective = str(input("adjective: "))
noun = str(input("noun: "))
verb = str(input("verb: "))
indoor_activity = str(input("indoor activity: "))
person = str(input("person: "))
outdoor_activity = str(input("outdoor activity: "))

input = {
    "adjective": adjective,
    "noun": noun,
    "verb": verb,
    "indoor_activity": indoor_activity,
    "person": person,
    "outdoor_activity": outdoor_activity
}

print(create_mad_lib(input))