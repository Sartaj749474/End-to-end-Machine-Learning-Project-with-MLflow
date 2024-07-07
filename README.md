# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows
Update config.yaml
Update schema.yaml
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the app.py


How to run?
STEPS:
Clone the repository
https://github.com/Dhach123/End-to-end-Machine-Learning-Project-with-MLflow


STEP 01- Create a conda environment after opening the repository
source ~/anaconda3/etc/profile.d/conda.sh
 virtualenv mlproj
conda activate mlproj
. mlproj/scripts/activate  
1)python -m venv mlproj   old
2)mlproj\Scripts\activate  old  

STEP 02- install the requirements
pip install -r requirements.txt


# Finally run the following command
python app.py

Now
open up you local host and port


# MLflow
DOCUMENT https://mlflow.org/docs/latest/index.html

# Command for MLFLOW
mlflow ui

# dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/Dhach123/End-to-end-Machine-Learning-Project-with-MLflow.mlflow
MLFLOW_TRACKING_USERNAME=Dhach123
MLFLOW_TRACKING_PASSWORD=ee4223cfcad036a1e48f4838e79d68a2a983aeea
python script.py


Run this to export as env variables:


export MLFLOW_TRACKING_URI=https://dagshub.com/Dhach123/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=Dhach123 

export MLFLOW_TRACKING_PASSWORD=ee4223cfcad036a1e48f4838e79d68a2a983aeea

