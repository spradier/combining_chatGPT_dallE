import os
import openai 
import pandas as pd
from flask import Flask, request, render_template

# Instantiate the app
app = Flask(__name__)

openai.api_key = 'YOUR-API-KEY'

def chat_gpt(prompt):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=4000,
      temperature=0.5
    )
    print(response['choices'][0]['text'])
    return response['choices'][0]['text']

def dall_e(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="512x512"
    )
    image_url = response['data'][0]['url']
    print(response['data'][0])
    return image_url

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
      return render_template('index.html')

    if request.method == "POST":
        text = request.form['text']
        processed_text = text.upper()
        return render_template('index.html', data=dall_e(chat_gpt(processed_text)))

if __name__ == '__main__':
    app.run()
