from src.textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
import os
import re  # Add this import at the top if not already present

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
        # Get absolute paths for Render compatibility
        project_root = os.path.abspath(os.path.dirname(__file__))
        self.model_path = os.path.join(project_root, self.config.model_path)
        self.tokenizer_path = os.path.join(project_root, self.config.tokenizer_path)
    
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        
        # Remove <n> tags from the summary output
        cleaned_output = re.sub(r"<n>", " ", output)
        
        print("\nModel Summary:")
        print(cleaned_output)

        return cleaned_output
