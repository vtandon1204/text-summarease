from flask import Flask, render_template, request, jsonify # type: ignore
from src.textSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

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
    app.run(host="0.0.0.0", port=5000,debug=True)
