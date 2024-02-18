from twilio.rest import Client
import os
import smtplib


# twilio_sid
account_sid = os.environ.get("account_sid")
# twilio_auth_token
auth_token = os.environ.get("auth_token")


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+18583608046",
            to="+917976677872"
        )

        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
