import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import openai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)

openai.organization = os.getenv("OPENAI_API_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")


def exchange(messages: list[dict[str, str]]) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=256,
        temperature=0.8
    )

    message = response.choices[0].message.content
    return message


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/chat", methods=["POST", "OPTIONS"])
@cross_origin()
def chat():
    data = request.get_json(force=True)
    messages = data.get("messages")
    print(messages)
    if not messages:
        resp = jsonify({"error": "Please provide a messages array"})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp, 400

    try:
        response_text = exchange(messages)
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
