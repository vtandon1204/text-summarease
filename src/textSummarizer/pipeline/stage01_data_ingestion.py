from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger
from pathlib import Path
class DataIngestionTrainingPipeline:  # Changed to class definition
    def __init__(self):
        pass
    
    def main(self):
        config_filepath = Path("config/config.yaml")
        params_filepath = Path("params.yaml")
        config = ConfigurationManager(config_filepath=config_filepath, params_filepath=params_filepath)  # type:ignore
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()