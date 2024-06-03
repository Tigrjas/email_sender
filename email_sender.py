import smtplib
import ssl
from email.message import EmailMessage
import dotenv
import os

# Define email sender and receiver
dotenv.load_dotenv()

email_sender = os.getenv("REPLACE")
email_password = os.getenv("REPLACE")
email_receiver = os.getenv("REPLACE")

# Set the subject and body of the email
email = {
    'subject': "REPLACE",
    'body': """
    REPLACE
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
    send_email(email_sender, email_password, email_receiver, email)
