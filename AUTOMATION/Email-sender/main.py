import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email from python"
sender_email = "coder.me08@gmail.com"
receiver_email = "coder.me08@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()