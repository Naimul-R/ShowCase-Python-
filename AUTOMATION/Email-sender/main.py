import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email from python"
sender_email = "coder.me08@gmail.com"
receiver_email = "coder.me08@gmail.com"
password = input("Enter a password: ")

