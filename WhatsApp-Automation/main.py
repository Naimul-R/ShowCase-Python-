# Import required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials
Accound_sid = "secret"
Auth_token = "secret"

client = Client(Accound_sid, Auth_token)

#Designe send message function 
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+141*********',
            body=message_body,
            to=f'Whatsapp: {recipient_number}'
        )

        print(f"Message sent successfully! message SID{message.sid}")

    except Exception as e:
        print(f"An error occurred!")

# User Input for recipient number and message
name = input("Enter the recipient's name: ")
recipient_number = input ("Enter the recipient's WhatsApp number with country code (e.g., +1234567890): ")
message_body =input(f'Enter the message you want to send to {name}: ')

# Parse date/time and calculate delay
date_str = input("Enter the date to send the nessage (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

#datetime
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The scheduled time is in the past. Please enter a future date and time.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

    #wait ubtil the scheduled time
    time.sleep(delay_seconds)

    #send the message
    send_whatsapp_message(recipient_number, message_body)
