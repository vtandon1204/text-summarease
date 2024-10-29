# import os

# path = 'D:/technical/AI-ML/ml_projects/text-summarizer-project/artifacts/data_transformation/samsum_dataset/test/data-00000-of-00001.arrow'

# directory = os.path.dirname(path)
# if not os.path.exists(directory):
#     print(f"Directory does not exist: {directory}")
# else:
#     print("Directory exists.")
# if len(path) > 260:
#     print("Path exceeds maximum length.")
from pathlib import Path
config_filepath = Path('config/config.yaml')
print(f"Config file path: {config_filepath}")
