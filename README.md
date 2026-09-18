## Live Demo

[Click here to try the Medical Insurance Cost Prediction App](https://medical-insurance-cost-prediction-5upp9g5tqmd2uu5nps94jr.streamlit.app/)# Medical Insurance Cost Prediction

## Project Overview

This project uses Machine Learning to predict estimated medical insurance costs based on personal and health-related information. A Linear Regression model is trained on the Medical Cost Personal Dataset and used to predict insurance charges for new inputs.

## Problem Statement

Medical insurance costs can vary depending on factors such as age, BMI, number of children, smoking status, gender, and region. The goal of this project is to build a machine learning model that can estimate insurance costs from these factors.

## Dataset

The project uses the Medical Cost Personal Dataset.

The dataset contains information about:

* Age
* Gender
* BMI
* Number of Children
* Smoking Status
* Region
* Insurance Charges

The target variable is **charges**, which represents the medical insurance cost.

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the original dataset using Pandas.
2. Checked the dataset information and data types.
3. Checked for missing values.
4. Identified and removed duplicate records.
5. Converted categorical variables into numerical form using one-hot encoding.
6. Prepared the final cleaned dataset for machine learning.

Categorical variables such as gender, smoker status, and region were encoded into numerical features.

## Features

The model uses the following input features:

* `age`
* `bmi`
* `children`
* `sex_male`
* `smoker_yes`
* `region_northwest`
* `region_southeast`
* `region_southwest`

The target variable is:

* `charges`

## Exploratory Data Analysis

Exploratory analysis was performed to understand the dataset and examine the relationship between the input features and insurance charges.

## Machine Learning Model

A **Linear Regression** model was selected for this project because the target variable, insurance charges, is numerical and the project focuses on predicting a continuous value.

## Model Training

The prepared dataset was divided into training and testing sets.

The Linear Regression model was then trained using the training data and used to make predictions on unseen test data.

## Model Evaluation

The trained model was evaluated using the following regression metrics:

| Metric   |      Result |
| -------- | ----------: |
| MAE      |     4177.05 |
| MSE      | 35478020.68 |
| RMSE     |     5956.34 |
| R² Score |      0.8069 |

The R² score indicates that the model explains approximately 80.69% of the variance in the test-set insurance charges.

## Prediction

The trained model can predict an estimated insurance cost for a new person based on their:

* Age
* BMI
* Gender
* Smoking status
* Number of children
* Region

## Streamlit Application

A Streamlit web application was created to provide an interactive interface for the trained model.

Users can enter their information and click the **Predict** button to receive an estimated medical insurance cost.

## Project Structure

```text
Medical-Insurance-Cost-Prediction/
│
├── app.py
├── insurance_model.pkl
├── requirements.txt
├── Medical_Insurance_Cost_Prediction.ipynb
└── README.md
```

## Limitations

* The prediction is an estimate and may not represent the actual insurance cost for an individual.
* The model is trained on the available dataset and may not generalize perfectly to other populations or insurance systems.
* Linear Regression may not capture all complex relationships between the input features and insurance charges.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Google Colab
* GitHub
