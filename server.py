from flask import Flask, request, jsonify
from google.generativeai import GoogleGenerativeAI

app = Flask(__name__)

# Configure your API key here
api_key = 'AIzaSyBUAbpX0IrfcHNZfFanELYhmAzSxrISssE'
genAI = GoogleGenerativeAI(api_key)
model = genAI.getGenerativeModel({'model': 'gemini-1.5-flash'})

generation_config = {
    'temperature': 1,
    'topP': 0.95,
    'topK': 64,
    'maxOutputTokens': 8192,
    'responseMimeType': 'text/plain',
}

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('input')

    # Define the content for the AI
    parts = [
        {'text': "당신은 사하중학교 AI입니다. 당신은 사하중학교 학생에게 사하중학교에 대하여 설명해주어야 합니다. 또한, 당신은 사하중학교 홈페이지 'https://school.busanedu.net/saha-m/main.do'를 참고 할 수 있습니다."},
        {'text': "input: "},
        {'text': user_input},
        {'text': "output: "},
    ]

    # Call the AI model
    result = model.generateContent({
        'contents': [{'role': 'user', 'parts': parts}],
        'generationConfig': generation_config,
    })

    output = result.response.text().strip()
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
