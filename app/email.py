import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

message = Mail(
    from_email= os.getenv("SENDER_EMAIL_ADDRESS"),
    to_emails= [To('nehasandesh14@gmail.com'), To('maddiepfister19@gmail.com')],
    subject='Subject line',
    text_content='This is the message of your email',
)

sg = os.getenv("SENDGRID_API_KEY")
response = sg.send(message)