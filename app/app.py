
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

userinput = input("Enter the roommate's email:")

while userinput != exit_loop:
    data["emails"].append(userinput)
    userinput = input("Enter the roommate's email:")

print(data)

## App Structure

import(random)

assignments{}

for member in data["members"]:
    assignments[member] = []

chores = data["chores"]

while len(chores) > 0:
    for member in data["members"]:
        task = random.choice(chores)
        chores.remove(task)
        assignments[member].append(task)

#for member in assignments:
    #email = input(f'Please enter {member}s email addresss:')
    #assignments[member]["email"] = email



for member in assignments:    
    print(member, ":", assignments[member])





