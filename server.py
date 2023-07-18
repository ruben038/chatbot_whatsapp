from flask import Flask, request,jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client



app = Flask(__name__)
ACCOUNT_SID = "AC885a41f08542801fa0d032d6fe093cb6"
AUTH_TOKEN = "552ad334d368cf7d45ff6dde3cf95d42"

# Create a Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)
def respond(msg):
    response =MessagingResponse()
    response.message(msg)
    return str(response)


@app.route('/msg')
def hello():
    message = client.messages.create(
    body="Welcome to GestStudents",
    to="whatsapp:+22966793237",
    from_="whatsapp:+14155238886",
    status_callback="https://dfad-41-85-163-66.ngrok-free.app/webhook")
    return message
    

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form.get('Body').lower()

    if data :
       
        # Faire quelque chose avec le contenu du message ici
        if data == "1":
            response_message = "Hello ruben"
        else:
            response_message = "Répondez avec le chiffre 1 pour obtenir le message de bienvenue."

      
        response_data = {
            'message': response_message
        }

        return respond(response_data)
if __name__ == '__main__':
    app.run(debug=True)
