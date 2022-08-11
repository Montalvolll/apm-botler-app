import hashlib
import hmac
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def reply():

    secret = 'qn7VoYDD6imwdFjjRmK0SexbRsgjpGoOgoboYHOjVqQ='
    encoded_secret = str.encode(secret)
    msg = request.form.get('Body')

    hashed = 'HMAC ' + hmac.new(encoded_secret, msg.encode('UTF-8'), hashlib.sha256).digest()
    # digested_value = body.digest()

    # if(msg.lower() == "hello"):
    if(hashed == request.headers.get('authorization')): #not yet finished...
    	if(msg == 'Hola'):
            reply = "Hi, this is an automated reply." 
        elif(msg == "APM"):
            reply = "Best of bests"
        else:
            reply = "Command not found."
    response = MessagingResponse()
    response.message(reply)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
