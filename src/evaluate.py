import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt

df = pd.read_csv(
    "dataset/placement_data.csv"
)

X = df.drop("Placed", axis=1)
y = df["Placed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = joblib.load(
    "models/placement_model.pkl"
)

predictions = model.predict(X_test)

cm = confusion_matrix(
    y_test,
    predictions
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.title(
    "Confusion Matrix"
)

plt.savefig(
    "screenshots/confusion_matrix.png"
)

print("Confusion matrix saved")

from sklearn.metrics import classification_report

print(
    classification_report(
        y_test,
        predictions
    )
)