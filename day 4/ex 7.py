from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
import pickle

df = pd.read_csv(r"C:\Users\chokk\Downloads\student-mat.csv", sep=';')

X = df[['studytime','failures','absences','age']]
y = df['G3']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train,y_train)

with open("model.pkl","wb") as file:
    pickle.dump(model,file)

print("Model Saved")
