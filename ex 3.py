from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv(r"c:\Users\chokk\Downloads\student-mat.csv", sep=';')

X = df[['studytime','failures','absences','age']]
y = df['G3']

for size in [0.1,0.2,0.3]:
    X_train,X_test,y_train,y_test = train_test_split(
        X,y,
        test_size=size,
        random_state=42
    )

    print(f"\nTest Size = {size}")
    print("Train Samples:",len(X_train))
    print("Test Samples :",len(X_test))