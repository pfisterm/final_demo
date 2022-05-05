
#create a function that takes in user inputs and returns assigned chores

def assign_chores():
    ## Data Inputs

    data = {"members": [], "chores": []}

    print("Please enter the names of all the roommates in the apartment. When finished enter exit.")

    print("--------------------------")

    exit_loop = "exit"
    userinput = input("Enter the name of the roommate:")

    while userinput != exit_loop:
        data["members"].append(userinput)
        userinput = input("Enter the name of the roommate:")
    
    print("--------------------------")

    print("Please enter all the chores that need to be completed. When finished please enter exit.")

    print("--------------------------")
        

    userinput = input("Enter the chore:")

    while userinput != exit_loop:
        data["chores"].append(userinput) 
        userinput = input("Enter the chore:")

    print("---------------------------")


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

    for member in assignments:
        tasks = assignments[member]["tasks"]
        chores = ' & '.join(', '.join(tasks).rsplit(', ', 1))
        print(f"{member}: {chores}")

    return assignments





    