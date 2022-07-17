import requests
import random

numbers = "1234567890"

url = "https://www.fast2sms.com/dev/bulkV2"

otp = ""
for _ in range(6):
    otp += random.choice(numbers)

number = input("Enter your mobile number: ")

querystring = {
    "authorization":"<your API key>",
    "message":f"your otp is: {otp}",
    "language":"english",
    "route":"q",
    "numbers": number
}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print("OTP sent to mobile.")

entered = input("Enter the OTP you received: ")
if entered == otp:
    print("You are authenticated.")
else:
    print("Incorrect OTP.")

# print(response.text)