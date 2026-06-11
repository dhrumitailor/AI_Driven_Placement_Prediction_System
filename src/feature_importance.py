import pandas as pd
import joblib
import matplotlib.pyplot as plt

model = joblib.load("models/placement_model.pkl")

df = pd.read_csv("dataset/placement_data.csv")

X = df.drop("Placed", axis=1)

importance = model.feature_importances_

plt.figure(figsize=(8,5))

plt.barh(
    X.columns,
    importance
)

plt.title("Feature Importance")
plt.xlabel("Importance Score")

plt.tight_layout()

plt.savefig(
    "screenshots/feature_importance.png"
)

print("Feature importance graph saved")