
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and label encoder
model = pickle.load(open('dropout_model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    features = []

    # Get all 34 input values
    for i in range(34):
        value = request.form.get(f'feature{i}', 0)
        features.append(float(value))

    features = np.array([features])

    # Prediction
    prediction = model.predict(features)

    # Confidence Score
    probability = model.predict_proba(features)
    confidence = round(np.max(probability) * 100, 2)

    # Convert label to text
    result = label_encoder.inverse_transform(prediction)[0]

    return render_template(
        'result.html',
        prediction=result,
        confidence=confidence
    )
if __name__ == '__main__':
    app.run(debug=True)