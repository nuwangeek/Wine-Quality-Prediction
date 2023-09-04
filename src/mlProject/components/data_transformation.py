import os
from mlProject import logger
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig
import pandas as pd 

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: Here we can add different data transformation techniques such as Scaler, PCA and all
    # And also can perform all kinds of EDA in ML cycle here before passing this data to the model

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)