import sys, os
from componentsDetection.logger import logging
from componentsDetection.exception import AppException
from componentsDetection.components.data_ingestion import DataIngestion
from componentsDetection.entity.config_entity import DataIngestionConfig
from componentsDetection.entity.artifacts_entity import DataIngestionArtifact



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        # self.data_validation_config = DataValidationConfig()
        # self.model_trainer_config = ModelTrainerConfig()
        
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            # data_validation_artifact = self.start_data_validation(
            #     data_ingestion_artifact=data_ingestion_artifact
            # )

            # if data_validation_artifact.validation_status == True:
            #     model_trainer_artifact = self.start_model_trainer()
                # else:
                # raise Exception("Your data is not in correct format")
        
        except Exception as e:
            raise AppException(e, sys)