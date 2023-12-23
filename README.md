# Credit Card Customer Churn Prediction

## Overview
This repository contains code and resources for predicting credit card customer churn. The project aims to analyze historical customer data and develop machine learning models to predict churn behavior.

## Table of Contents
- [Project Background](#project-background)
- [Data](#data)
- [Methodology](#methodology)
  - [Data Preprocessing](#data-preprocessing)
  - [Feature Engineering](#feature-engineering)
  - [Model Training](#model-training)
  - [Evaluation](#evaluation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Project Background
- This project centers on leveraging machine learning techniques to predict credit card customer churn. 
- By analyzing historical data encompassing transaction behavior, demographics, and usage patterns, the aim is to develop predictive models that identify potential churners. 
- The project seeks to empower financial institutions with proactive insights, enabling targeted retention strategies and enhancing overall customer satisfaction and loyalty in the competitive credit card industry.

## Data
- Data is taken from Kaggle , it contains a csv file "BankChurners.csv".
  - it has 22 feature columns , which gives out vrious personal information like age ,gender, educationa nd martial status along with their financial activity and status like income and daily/monthly/quaterly usages.
  - it's target column is "Attrition_Flag" which contains binary data indiacting weather the customer is churned or not.
    
- data source :- https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

## Methodology


#### Data Preprocessing
Outline the steps taken to clean and preprocess the data. Include any data transformations, handling missing values, and scaling or normalization.

#### Feature Engineering
Explain the process of creating new features or selecting relevant features for the churn prediction model.

#### Model Training
Detail the steps involved in training machine learning models. Discuss the algorithms used, hyperparameter tuning, and model selection techniques. Provide code snippets or references to the training scripts/notebooks.

#### Evaluation
Explain how the models were evaluated. Discuss the metrics used to assess model performance and how well the models predict churn.

## Usage
Create a conda environment using environment file , activate that environment and the run the app.py file.
if run sucessfully, you should be able to access the web app at localhost.
you can also explore the notebook file (analysis.ipynb).

Example:-   
```
# clone repo
git@github.com:0x1h0b/CustomerBankData-Segmentation.git

# create environment
conda env create --name <envname> --file=environments.yml

# activate env
conda activate <envname>

# run app.py
python app.py

```

## Results
Present the findings and results of the churn prediction model. Discuss model performance metrics, any insights gained from the analysis, and potential business implications.


## License

MIT License | Copyright (c) 2023 Himanshu Bag

A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

