# Student Dropout Prediction Project (Day 13 Final Project)

## Project Title
Student Academic Performance Prediction System using Machine Learning and Flask

## Project Objective
This project predicts whether a student will Graduate, be Enrolled, or Dropout based on academic and personal features using Machine Learning.

## Classes Predicted
- Graduate  
- Enrolled  
- Dropout  

## Machine Learning Model
- Algorithm: Logistic Regression / Random Forest  
- Library: Scikit-learn  
- Model File: model.pkl  

## Features Used
- Age  
- Enrollment Status  
- Gender  
- Marital Status  
- Tuition Fees Status  
- Scholarship Holder  
- 1st Semester Approved Subjects  
- 1st Semester Grade  
- 2nd Semester Approved Subjects  
- 2nd Semester Grade  
- Debtor Status  

## Technologies Used
- Python  
- Flask  
- HTML  
- CSS  
- Pandas  
- NumPy  
- Scikit-learn  

## Project Workflow
- Data collection and preprocessing  
- Model training  
- Model saving using pickle  
- Flask web app development  
- Connecting ML model with Flask  
- Taking user input through web form  
- Predicting student outcome  

## How to Run the Project
1. Install dependencies:
   pip install -r requirements.txt

2. Run Flask application:
   python app.py

3. Open browser:
   http://127.0.0.1:5000/

## Project Structure
student-dropout-project/
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── screenshots/
    ├── graduate.png
    ├── enrolled.png
    └── dropout.png

## Output
The system provides predictions in three categories:
Graduate, Enrolled, and Dropout.

## Author
Internship Final Project - Day 13 Submission
