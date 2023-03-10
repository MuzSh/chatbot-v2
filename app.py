from flask import Flask, request, render_template
import requests
import os 
from dotenv import load_dotenv
import re

yearList = [] 

def configure():
    load_dotenv()
    
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    configure()
    user_message = request.args.get('msg')
    if user_message in ['What is your name?', 'name?']:
        response = "My name is ChatBot."
    elif user_message in ['How old are you?', 'age?']:
        response = "I don't have an age, I'm just a computer program."
    else:
        api_key = os.getenv('api_key')
        model = "text-curie-001"
        response = generate_response_gpt3(user_message, model, api_key)
        # for i in range(25):
            # response = generate_response_gpt3(user_message, model, api_key)
            # print(response)
            # try:
            #     val = [int(year_regex.search(string).group(response)) for string in yearList ]
            #     yearList.append(val)
            # except:
            #     pass
    return response

def generate_response_gpt3(user_message, model, api_key):
    prompt = (f"User: {user_message}\n"
              f"ChatBot:")
    response = requests.post(
        "https://api.openai.com/v1/engines/text-curie-001/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.7,
        },
    ).json()

    # print(response['choices'][0]['text'].strip())

    # some error handling 

    if 'error' in response:
        keyWords = ['exceeded', 'quota']
        result = response["error"]["message"]
        if any(word in str(result) for word in keyWords):
            return "No More. Please contact your administrator for more information!"
        else:
            return f"Sorry, there was an error processing your request. Please try again later."
    return response['choices'][0]['text'].strip()

if __name__ == "__main__":
    app.run()
    # year_regex = re.compile(r'\d{4}')  # Regular expression to match four consecutive digits
    # years = [int(year_regex.search(string).group()) for string in yearList]
    # print(years)