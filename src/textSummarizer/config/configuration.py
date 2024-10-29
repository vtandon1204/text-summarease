from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig)   
from textSummarizer.entity import (DataValidationConfig)
from textSummarizer.entity import (DataTransformationConfig)


class ConfigurationManager:
    def __init__(self, 
                 config_filepath: Path = Path("config/config.yaml"), 
                 params_filepath: Path = Path("params.yaml")):
        self.config = read_yaml(config_filepath)  # Ensure this returns a dictionary
        self.params = read_yaml(params_filepath)
        create_directories([Path(self.config['artifacts_root'])])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config =  DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        if 'data_validation' not in self.config:
            raise AttributeError("data_validation section missing in config.yaml")

        config = self.config['data_validation']  # Access as a dictionary
        create_directories([Path(config['root_dir'])])  # Ensure directory exists

        return DataValidationConfig(
            root_dir=Path(config['root_dir']),  # Ensure it's a Path object
            STATUS_FILE=config['STATUS_FILE'],
            ALL_REQUIRED_FILES=config['ALL_REQUIRED_FILES'],
        )
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config