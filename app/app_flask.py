import sys
import os

# Determine the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.textSummarizer.pipeline.prediction import PredictionPipeline
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

# Initialize the prediction pipeline
predictor = PredictionPipeline()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Generate summary
    summary = predictor.predict(text)

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
