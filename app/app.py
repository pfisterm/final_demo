

data = {"number": "L21", "members": ["Catie", "Maddie", "Meher", "Nina", "Rebecca"], 
"chores": ["vaccuming", "kitchen counters", "stove", "kitchen and dining table", 
"kitchen sink", "bathroom counter", "mirror", "showers", "toilets", "trash and recycling"] }

import random

chores = data["chores"]

for member in data["members"]:
    task_1 = ''.join(random.sample(chores, 1))
    chores.remove(task_1)
    task_2 = ''.join(random.sample(chores, 1))
    chores.remove(task_2)
    print(member, ":", task_1, ",", task_2)
