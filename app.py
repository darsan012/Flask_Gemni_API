from flask import Flask, request
from gemniconfig import gemini_model
import os

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
PORT = os.getenv("PORT")

@app.route('/')
def home():
    return "Welcome. App is running successfully."

@app.route("/chat", methods=["POST"])
def chat():
    # Getting JSON data from POST request
    data = request.json

    # Extracting the "prompt" from the JSON data
    prompt = data["prompt"]

    # Calling the function "gemini_model" in the gemini_api.py
    output = gemini_model(user_prompt=prompt)

    # Returning the model response as the output
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)