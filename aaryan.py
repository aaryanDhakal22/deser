import smtplib
import sys

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com",
}

EMAIL = "williamsbottified@gmail.com"
PASSWORD = "feux lmsw xcsq bggm"


def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.set_debuglevel(debuglevel=0)
    server.starttls()
    server.login(auth[0], auth[1])
    print(auth[0], recipient, message)
    server.sendmail(auth[0], recipient, message)
    server.quit()


send_message("4437568987", "tmobile", "Hello")
