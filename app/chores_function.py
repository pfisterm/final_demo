#Adjusted chores function to run on web app

def chores(data = dict()):

    import random

    assignments = dict()

    for member in data["members"]:
        assignments[member] = []

    for member in assignments:
        assignments[member] = dict()
        assignments[member]["tasks"] = []
        email = input(f'Please enter the email for {member}:')
        assignments[member]["email"] = email


    chores = data["chores"]

    while len(chores) > 0:
        for member in assignments:
            task = random.choice(chores)
            chores.remove(task)
            assignments[member]["tasks"].append(task)

    for member in assignments:
        tasks = assignments[member]["tasks"]
        chores = ' & '.join(', '.join(tasks).rsplit(', ', 1))
        print(f"{member}: {chores}")

    return assignments
