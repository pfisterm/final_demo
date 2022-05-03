
#create a function that takes in user inputs and returns assigned chores

def assign_chores():
    ## Data Inputs

    data = {"number": "L21", "members": [], 
    "chores": [], "emails":[]}

    #three inputs: members, chores, emails
    #three keys, 5, 10, 5 values

    exit_loop = "exit"
    userinput = input("Enter the name of the roommate:")

    while userinput != exit_loop:
        data["members"].append(userinput)
        userinput = input("Enter the name of the roommate:")
        

    userinput = input("Enter the chore:")

    while userinput != exit_loop:
        data["chores"].append(userinput) 
        userinput = input("Enter the chore:")




    ## App Structure

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

    return print(assignments)






    