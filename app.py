from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# 🔑 Replace with your OpenAI API key or HuggingFace endpoint
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("question")

    # 🧠 Send prompt to OpenAI (or any LLM)
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"You are a coding assistant. {user_input}",
        max_tokens=150,
        temperature=0.7
    )

    answer = response.choices[0].text.strip()
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(port=5000)
