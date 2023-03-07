from flask import Flask, request, jsonify, render_template
import requests
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/get") 

def get_bot_response():
    user_message = request.args.get("msg")
    api_key = os.getenv('API_KEY')
    model = "text-davinci-003"
    respone = generate_response_gpt3(user_message,model,api_key)

def generate_response_gpt3(user_message,model,api_key):
    prompt = (f"User: {user_message}\n"f"chatbot:")
    response = requests.post("https:api.openai.com/v1/engines/text-davinci-003/completions",
                             headers={"Authorization": f"Bearer {api_key}"},
                             json= {
                                "prompt": prompt,
                                "max_tokens": 200,
                                "temperature": 0.7,
                             }).json()
    return response["choices"][0]['text'].strip()[]
#  run the app
if __name__ == "__main__":
    app.run(debug=True)
