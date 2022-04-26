

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


#############


import random

chores = data["chores"]

for member in data["members"]:
    task_1 = ''.join(random.sample(chores, 1))
    chores.remove(task_1)
    task_2 = ''.join(random.sample(chores, 1))
    chores.remove(task_2)
    print(member, ":", task_1, ",", task_2) 