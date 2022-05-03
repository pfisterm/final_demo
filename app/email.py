
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.chores import assign_chores

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")


def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>", recipient_address=SENDER_EMAIL_ADDRESS):
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


if __name__ == "__main__":

    assignments = {}

    assignments = assign_chores()

    print(type(assignments))

    #for member in assignments:

    example_subject = "Weekly Chore Assignment"

    for member in assignments:
        example_recipient_address = assignments[member]["email"]

        example_html = f"""
        <h3>These are your following chores for the week</h3>

        <h4>Today's Date</h4>
        <p>Monday, January 1, 2040</p>

        <h4>My Chores</h4>
        <ul>
            <var>assignments[member]["tasks"]</var>
        </ul>

            """

        print(send_email(example_subject, example_html, example_recipient_address))
