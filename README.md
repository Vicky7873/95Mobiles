# 95Mobiles

1. create a virtual env
conda create -n 95m python=3.12 -y
2. Create an log file
3. Create an project str
4. install dependencies
pip install -r requirements.txt

# Bike Price Predictions
1. Exp done for end to end
2. data ingestion for bike done
3. feature eng done
4. data splitting done
5. Hyper parameter tuninng with mlflow
![alt text](image.png)
6. model evaluatuion done with mlflow
![alt text](image-1.png)
7. Application added
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)


# Car price prediction
1. Exp done for end to end
2. data ingestion for bike done
3. feature eng done
4. data splitting done
5. Hyper parameter tuninng with mlflow
![alt text](image-5.png)
6. model evaluatuion done with mlflow
![alt text](image-6.png)
7. Application added

# DVC 
1. dvc init
2. dvc status
3. dvc dag
4. dvc repro


# Add git hooks
## git hook cmds
1. cd .git/hooks
2. nano pre-commit
save ->control+o, press enter then control+x for exist
3.#!/bin/bash

echo "Pre-commit hook triggered."
dvc repro
status=$?
##### Check

