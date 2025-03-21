import sys
import os

# Determine the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.textSummarizer.pipeline.prediction import PredictionPipeline
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Initialize the prediction pipeline
predictor = PredictionPipeline()

from flask import send_from_directory

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Invalid request"}), 400

        text = data["text"].strip()
        if not text:
            return jsonify({"error": "No text provided"}), 400

        summary = predictor.predict(text)
        return jsonify({"summary": summary})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render uses dynamic ports
    app.run(host="0.0.0.0", port=port, debug = False)  # Allow external access
