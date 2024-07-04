import os
from mlProject import logger
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        X_train, X_test = train_test_split(data)

        X_train.to_csv(os.path.join(self.config.root_dir, "X_train.csv"),index = False)
        X_test.to_csv(os.path.join(self.config.root_dir, "X_test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(X_train.shape)
        logger.info(X_test.shape)

        print(X_train.shape)
        print(X_test.shape)