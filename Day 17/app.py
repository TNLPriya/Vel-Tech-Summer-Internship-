from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import os

app = Flask(__name__)

# ---------------- DATABASE CONFIG ---------------- #

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------- LOAD MODEL ---------------- #

model = pickle.load(open('dropout_model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

# ---------------- DATABASE TABLE ---------------- #

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    scholarship = db.Column(db.Integer)
    prediction = db.Column(db.String(100))
    confidence = db.Column(db.Float)

# ---------------- HOME PAGE ---------------- #

@app.route('/')
def home():
    return render_template('index.html')

# ---------------- PREDICTION ---------------- #

@app.route('/predict', methods=['POST'])
def predict():

    try:

        age = float(request.form['age'])
        gender = int(request.form['gender'])
        marital_status = int(request.form['marital_status'])
        debtor = int(request.form['debtor'])
        tuition = int(request.form['tuition'])
        scholarship = int(request.form['scholarship'])

        first_sem_approved = float(request.form['first_sem_approved'])
        first_sem_grade = float(request.form['first_sem_grade'])
        second_sem_approved = float(request.form['second_sem_approved'])
        second_sem_grade = float(request.form['second_sem_grade'])

        # Create 34-feature array
        features = [0] * 34

        features[0] = marital_status
        features[14] = debtor
        features[15] = tuition
        features[16] = gender
        features[17] = scholarship
        features[18] = age
        features[22] = first_sem_approved
        features[23] = first_sem_grade
        features[28] = second_sem_approved
        features[29] = second_sem_grade

        final_features = np.array([features])

        prediction = model.predict(final_features)

        probabilities = model.predict_proba(final_features)

        confidence = round(max(probabilities[0]) * 100, 2)

        result = label_encoder.inverse_transform(prediction)[0]

        student = Student(
            age=age,
            gender=gender,
            scholarship=scholarship,
            prediction=result,
            confidence=confidence
        )

        db.session.add(student)
        db.session.commit()

        return render_template(
            'result.html',
            prediction=result,
            confidence=confidence
        )

    except Exception as e:
        return render_template(
            'result.html',
            prediction="Error",
            confidence=0,
            error=str(e)
        )

# ---------------- STUDENT RECORDS ---------------- #

@app.route('/customers')
def customers():

    students = Student.query.all()

    return render_template(
        'customers.html',
        students=students
    )

# ---------------- ABOUT ---------------- #

@app.route('/about')
def about():
    return render_template('about.html')

# ---------------- CREATE DATABASE ---------------- #

with app.app_context():
    db.create_all()

# ---------------- RUN APP ---------------- #

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)