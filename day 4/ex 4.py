from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

import pandas as pd
import numpy as np

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

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)

print("RMSE =",np.sqrt(mse))
print("R2 =",r2_score(y_test,y_pred))

new_student = [[3,0,2,17]]

print(
    "Predicted Grade:",
    model.predict(new_student)[0]
)
