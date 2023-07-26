import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
import imghdr
load_dotenv()


def send_emails(image_path):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv('GMAIL_SMTP_PASSWORD')
    username = os.getenv('GMAIL')
    receiver = username

    email_message = EmailMessage()
    email_message['Subject'] = "New morda showed up!"
    email_message.set_content('Hey, we just saw a something strange!')

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP(host, 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_emails("images/22.png")