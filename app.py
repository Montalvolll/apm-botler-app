from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def reply():
    msg = request.form.get('Body')
    # if(msg.lower() == "hello"):
    if(msg == "julio"):
    	reply = "Se la comeeee" 
    elif(msg == "Julio"):
    	reply = "Porrooon"
    else:
        reply = "No se que putas responder"
    response = MessagingResponse()
    response.message(reply)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
