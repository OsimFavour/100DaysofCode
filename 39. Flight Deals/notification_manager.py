from twilio.rest import Client

TWILIO_SID = "ACd5ce2519eb0b307901fdb28b4039c912"
TWILIO_AUTH_TOKEN = "d01ae7c1593dc11ff09e14aae1101f47"
TWILIO_VIRTUAL_NUMBER = "+17076753490"
TWILIO_VERIFIED_NUMBER = "+2348130039337"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
