import random
from email.message import EmailMessage
import ssl
import smtplib
import json

with open('data.json', 'r') as f:
    data = json.load(f)

email_sender = data["email"]
email_password = data["password"]
email_receiver = ''

subject = 'Greetings User!'

body = ""

numbers = "1234567890"

email_receiver = input("Enter Your email id: ")

otp = ''

for i in range(6):
    otp += random.choice(numbers)

body = f"Your OTP is: {otp}."

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
# em.set_content(body)

html = f"""
<html>
    <body>
        <h1>Greetings user!</h1>
        <p>Your OTP is <b>{otp}</b>. Please enter it in application to get verified.</p>
    </body>
</html>
"""

em.add_alternative(html, subtype="html")

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("OTP sent to mail.")

entered = input("Enter the OTP you received: ")

if entered == otp:
    print("Successfully verified")