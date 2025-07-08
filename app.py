from flask import Flask, request, jsonify
from transformers import pipeline
# app.py additions
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <--- add this line to enable CORS for all routes

# Load your fine-tuned GPT-2 model
model_path = "./gpt2-tasker"
generator = pipeline("text-generation", model=model_path, tokenizer=model_path)

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    user_input = data.get("prompt", "")
    
    # Format the prompt as expected by your fine-tuned model
    prompt = f"User: {user_input.strip()}\nAssistant:\n"

    result = generator(
        prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=50256  # Needed to avoid warning for GPT-2
    )

    generated_text = result[0]["generated_text"]
    
    # Extract only the part after "Assistant:"
    response_only = generated_text.split("Assistant:\n", 1)[-1].strip()

    return jsonify({"response": response_only})

if __name__ == '__main__':
    app.run(debug=True)

