

# IMPORT LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ============================================
# LOAD DATASET
# ============================================

# IMPORTANT: sep="\t" for tab-separated dataset

df = pd.read_csv("train.csv", sep="\t")

print("\nFIRST 5 ROWS:\n")

print(df.head())

print("\nDATASET INFO:\n")

print(df.info())

print("\nMISSING VALUES:\n")

print(df.isnull().sum())

# ============================================
# ENCODE CATEGORICAL COLUMNS
# ============================================

le = LabelEncoder()

categorical_cols = df.select_dtypes(include=['object', 'string']).columns

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# ============================================
# DEFINE FEATURES AND TARGET
# ============================================

X = df.drop("final_score", axis=1)

y = df["final_score"]

# ============================================
# SPLIT DATA
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ============================================
# TRAIN MODEL
# ============================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nMODEL TRAINED SUCCESSFULLY")

# ============================================
# MAKE PREDICTIONS
# ============================================

predictions = model.predict(X_test)

print("\nPREDICTIONS:\n")

print(predictions[:10])

# ============================================
# MODEL EVALUATION
# ============================================

mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nMAE :", mae)

print("R2 SCORE :", r2)

# ============================================
# FEATURE IMPORTANCE
# ============================================

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importance
})

feature_importance = feature_importance.sort_values(
    by='Importance',
    ascending=False
)

print("\nFEATURE IMPORTANCE:\n")

print(feature_importance)

# ============================================
# FEATURE IMPORTANCE GRAPH
# ============================================

plt.figure(figsize=(10,6))

sns.barplot(
    x='Importance',
    y='Feature',
    data=feature_importance
)

plt.title("Feature Importance")

plt.show()

# ============================================
# SAVE MODEL
# ============================================

joblib.dump(model, "student_score_prediction.pkl")

print("\nMODEL SAVED SUCCESSFULLY")

# ============================================
# SAMPLE PREDICTION
# ============================================

sample = X_test.iloc[0:1]

prediction = model.predict(sample)

print("\nPREDICTED SCORE :", prediction[0])

print("ACTUAL SCORE :", y_test.iloc[0])

# ============================================
# END
# ============================================