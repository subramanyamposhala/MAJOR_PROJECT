from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = 'http://127.0.0.1:5005/webhooks/rest/webhook'


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)
    
    # Send the user message to RASA API and get the response
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()
    
    print("Rasa response:", rasa_response_json)

    # Get the bot's response or provide a fallback message
    bot_response = rasa_response_json[0]['text'] if rasa_response_json else "Sorry, I am not trained for this! :("

    # Return the bot's response
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)







