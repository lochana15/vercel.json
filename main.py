import os
from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

ACOUNT_SID = "ACedddd78041e2ef37db22ddb717bafeca"
AUTH_TOKEN = "94eec8db309590df3bbbdedc89ca86a4"

client = Client(ACOUNT_SID, AUTH_TOKEN)


@app.route("/sms", methods=["GET"])
def sms():
    to = request.args.get("to")
    client.messages.create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_="+15098225799",
        to="+918095296336",
    )
    return {"status": "success"}


if __name__ == "__main__":
    app.run(debug=True)
