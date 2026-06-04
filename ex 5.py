from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\chokk\Downloads\student-mat.csv", sep=';')

features = [
    'studytime',
    'failures',
    'absences',
    'G1'
]

for feature in features:

    X = df[[feature]]
    y = df['G3']

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            y_pred
        )
    )

    print(feature,"RMSE =",rmse)