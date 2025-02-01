class Notification:
    def send(self   ):
        print(f"Notification")

class EmailNotification:
    def send(self):
        print("You got an email")

class SMSNotification:
    def send(self):
        print("You got an SMS")

email=EmailNotification()
email.send()
sms=SMSNotification()
sms.send()