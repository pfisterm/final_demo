

data = {"members": ["Catie", "Maddie", "Meher", "Nina", "Rebecca"], 
"chores": ["vaccuming", "kitchen counters", "stove", "kitchen and dining table", 
"kitchen sink", "bathroom counter", "mirror", "showers", "toilets", "trash and recycling"]}


import random

chores = data["chores"]

assignments = {}

for member in data["members"]:
    assignments[member] = []

while len(chores) > 0:
    for member in data["members"]:
        task = ''.join(random.choice(chores))
        chores.remove(task)
        assignments[member].append(task)

for member in assignments:
    email = input(f'Please enter {member}s email addresss:')
    #assignments[member]["email"] = email

print(assignments)
