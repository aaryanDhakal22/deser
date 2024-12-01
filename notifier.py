import requests

# importing os module for environment variables
import os

# importing necessary functions from dotenv library
from dotenv import load_dotenv

# loading variables from .env file
load_dotenv()

# accessing and printing value
APP_TOKEN = os.getenv("APP_TOKEN")
aaryan = os.getenv("aaryan")


def send_notification(message, image_path):
    r = requests.post(
        "https://api.pushover.net/1/messages.json",
        data={"token": APP_TOKEN, "user": aaryan, "message": message},
        files={"attachment": ("card.jpg", open(image_path, "rb"), "image/jpeg")},
    )
    print(r.text)


# r = requests.post(
#     "https://api.pushover.net/1/messages.json",
#     data={"token": APP_TOKEN, "user": aaryan, "message": "There is a card"},
#     files={"attachment": ("card.jpg", open("card.jpg", "rb"), "image/jpeg")},
# )
# print(r.text)

# def send_notification(message):
#     conn = http.client.HTTPSConnection("api.pushover.net:443")
#     conn.request(
#         "POST",
#         "/1/messages.json",
#         urllib.parse.urlencode(
#             {
#                 "token": APP_TOKEN,
#                 "user": aaryan,
#                 "message": message,
#             }
#         ),
#         {"Content-type": "application/x-www-form-urlencoded"},
#     )
#     conn.getresponse()
