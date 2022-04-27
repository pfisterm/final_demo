
## Data Inputs

data = {"number": "L21", "members": [], 
"chores": [], "emails":[]}

#three inputs: members, chores, emails
#three keys, 5, 10, 5 values

exit_loop = "exit"
userinput = input("Enter the name of the roommate:")

while userinput != exit_loop:
    data["members"].append(userinput)
    email = input(f'Please enter the email for {userinput}:')
    data["emails"].append(email)
    userinput = input("Enter the name of the roommate:")
    

userinput = input("Enter the chore:")

while userinput != exit_loop:
    data["chores"].append(userinput) 
    userinput = input("Enter the chore:")


print(data)

## App Structure

import random

assignments = dict()

for member in data["members"]:
    assignments[member] = []

#for member in assignments:
   #assignments[member] = dict()
    #member["email"] = []

print(assignments)

#for member in data["member"]:
    #assignments[member]["email"].append(data["emails"])


chores = data["chores"]

while len(chores) > 0:
    for member in data["members"]:
        task = random.choice(chores)
        chores.remove(task)
        assignments[member].append(task)



for member in assignments:    
    print(member, ":", assignments[member])





