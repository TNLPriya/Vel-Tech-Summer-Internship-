# Course Dropout Early Warning System

## Project Overview

The Course Dropout Early Warning System predicts whether a student is likely to:

- Graduate
- Enrolled
- Dropout

The project uses Machine Learning techniques to analyze academic, demographic, and enrollment-related factors and provide early warnings for students at risk of dropping out.

---

## Dataset

Dataset: UCI Predict Students Dropout and Academic Success Dataset

Target Classes:
- Graduate
- Enrolled
- Dropout

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn

---

## Project Structure

├── model.py
├── predict.py
├── charts.py
├── dropout_model.pkl
├── label_encoder.pkl
├── target_distribution.png
├── age_distribution.png
├── correlation_heatmap.png
├── requirements.txt
└── README.md

---

## Features

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Multi-class Classification using XGBoost
- Model Evaluation
- Model Saving using Pickle
- Student Outcome Prediction
- Data Visualization

---

## Model

Algorithm Used:
XGBoost Classifier

Output Classes:
- Graduate
- Enrolled
- Dropout

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run model training:

python model.py

Run prediction:

python predict.py

Generate charts:

python charts.py

---

## Results

Successfully trained a multi-class classification model to predict student academic outcomes and saved the trained model as dropout_model.pkl.

---

## Author

Priya 
Vel Tech University
