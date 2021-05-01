from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# instansiasi kelas
app = Flask(__name__)

# akan menampilkan hello world saat app digunakan


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))
    # resp.message("Total kasus 1,67 jt kasus")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
