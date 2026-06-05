import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier

# LOAD DATASET
df = pd.read_csv(r"c:\Users\chokk\Downloads\dataset.csv")

print("Dataset Shape:", df.shape)

# TARGET ENCODING
le = LabelEncoder()
df["Target"] = le.fit_transform(df["Target"])

# FEATURES AND TARGET
X = df.drop("Target", axis=1)
y = df["Target"]

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# MODEL
model = XGBClassifier(
    objective="multi:softprob",
    num_class=3,
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train, y_train)

# PREDICTIONS
y_pred = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# SAVE MODEL
with open("dropout_model.pkl", "wb") as f:
    pickle.dump(model, f)

# SAVE LABEL ENCODER
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("\nModel Saved Successfully!")