import smtplib
import ssl
from email.message import EmailMessage
import dotenv
import os

# Define email sender and receiver
dotenv.load_dotenv()

email_sender = os.getenv("REPLACE with email address")
email_password = os.getenv("REPLACE with password")
email_receiver = 'REPLACE with receivers email'

# Set the subject and body of the email
subject = 'Enter Subject Text Here'
body = """
Enter Body Text here
"""
email = {
    'subject': "REPLACE subject here",
    'body': """
    REPLACE Body here
    """,
}


def send_email(sender: str, receiver: str, password: str, email: dict) -> None:
    message = EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Try to log in and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, message.as_string())
    except Exception as e:
        print("Email not send. Error: {e}")


if __name__ == "__main__":
    send_email(email_sender, email_receiver, password)
