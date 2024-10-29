from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger
from pathlib import Path

config_filepath = Path("config/config.yaml")  # Set the path to your config file
params_filepath = Path("params.yaml")

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager(config_filepath=config_filepath, params_filepath=params_filepath)
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()