import pandas as pd
import os
from mlProject import logger
import xgboost as xg
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        xgb_r = xg.XGBRegressor(n_estimators= self.config.n_estimators, seed = self.config.seed)
                  
        xgb_r.fit(train_x, train_y)

        joblib.dump(xgb_r, os.path.join(self.config.root_dir, self.config.model_name))