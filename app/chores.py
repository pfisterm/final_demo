
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



import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")

def send_email(subject="Assigned Chore Schedule", text, recipient_address):
    """
    Sends an email with the specified subject and html contents to the specified recipient,

    If recipient is not specified, sends to the admin's sender address by default.
    """
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)

    message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", type(e), e)
        return None

for member in assignments:
    send_email(subject=subject, text=assignments[member]["tasks"], recipient_address=assignments[member]["email"])


if __name__ == "__main__":
    assignchores()

    example_subject = "Assigned Chore Schedule"

    example_html = f"""
    <h3>Here are your assigned chores for the week</h3>

    <h4>Today's Date</h4>
    <p>Monday, January 1, 2040</p>

    <h4>Your Chores</h4>
    <ul>
        <li>Kitchen</li>
        <li>Bathroom</li>
        <li>Sweeping</li>
    </ul>

    <h4>My Forecast</h4>
    <ul>
        <li>10:00 AM | 65 DEGREES | CLEAR SKIES</li>
        <li>01:00 PM | 70 DEGREES | CLEAR SKIES</li>
        <li>04:00 PM | 75 DEGREES | CLEAR SKIES</li>
        <li>07:00 PM | 67 DEGREES | PARTLY CLOUDY</li>
        <li>10:00 PM | 56 DEGREES | CLEAR SKIES</li>
    </ul>
    """

    print(send_email(example_subject, example_html))


    