from twilio.rest import TwilioRestClient
import time

auth_sid = "<your account Sid here>"
auth_token = "<your auth token here>"

client = TwilioRestClient(auth_sid,auth_token)

if client:
    print "Authenticated"

def sendmsg(body):
    message = client.messages.create(body=body+"\n\t--Krishna Manoj Varanasi",to="+918790763112",from_="+12024992570")
    print "From Manoj",client.messages.get(message.sid).status

def getValues():
    f = open("christmasQuotes.txt","r")
    for quote in f.readlines():
        sendmsg(quote)
        time.sleep(10)

if __name__ == "__main__":
    getValues()
