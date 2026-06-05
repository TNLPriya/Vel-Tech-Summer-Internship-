import pickle
import pandas as pd

model = pickle.load(open("dropout_model.pkl", "rb"))
encoder = pickle.load(open("label_encoder.pkl", "rb"))

df = pd.read_csv(r"c:\Users\chokk\Downloads\dataset.csv")

sample = df.drop("Target", axis=1).iloc[0:1]

prediction = model.predict(sample)

result = encoder.inverse_transform(prediction)

print("Prediction:", result[0])