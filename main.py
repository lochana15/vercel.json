import os
from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

ACOUNT_SID = "ACedddd78041e2ef37db22ddb717bafeca"
AUTH_TOKEN = "fe3359325839ac8bf55e31d0daeade2f"

client = Client(ACOUNT_SID, AUTH_TOKEN)


@app.route("/sms", method=["GET"])
def sms():
    to = request.args.get("to")
    client.messages.create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_="+15098225799",
        to=to,
    )
    return {"status": "success"}


if __name__ == "__main__":
    app.run(debug=True)
