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
MLFLOW_TRACKING_PASSWORD=590f33406c061585e5596e6f4e56b0955f15843d
python script.py


Run this to export as env variables:


export MLFLOW_TRACKING_URI=https://dagshub.com/Dhach123/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=Dhach123 

export MLFLOW_TRACKING_PASSWORD=590f33406c061585e5596e6f4e56b0955f15843d


# AWS-CICD-Deployment-with-Github-Actions

1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 975050312709.dkr.ecr.eu-north-1.amazonaws.com/mlproj
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
About MLflow
MLflow

Its Production Grade
Trace all of your expriements
Logging & tagging your model
End-to-end-Machine-Learning-Project-with-MLflow/README.md at main · entbappy/End-to-end-Machine-Learning-Project-with-MLflow

