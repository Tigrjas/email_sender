import smtplib
import ssl
from email.message import EmailMessage
import dotenv
import os
import sys

# Define email sender and receiver
dotenv.load_dotenv()

email_sender = os.getenv("email_sender")
email_password = os.getenv("password")
email_receiver = os.getenv("email_receiver")

# Set the subject and body of the email
email = {
    'subject': "subject line",
    'body': """
    body text
    """,
}


def send_email(sender: str, password: str, receiver: str, email: dict) -> None:
    message = EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = email['subject']
    message.set_content(email['body'])

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
    if len(sys.argv) < 1:
        send_email(email_sender, email_password, email_receiver, email)
    elif len(sys.argv) == 4:
        email_receiver = sys.argv[1]
        subject = sys.argv[2]
        body = sys.argv[3]
        email = {
            'subject': subject,
            'body': body
        }
        send_email(email_sender, email_password, email_receiver, email)
    else:
        print("""
        To use command line feature there must be 3 arguments following the script:
            1. email receiver
            2. subject line
            3. body

        Example command:
        python email_receiver.py john@gmail.com Greetings "It was nice to meet you"
        """)
