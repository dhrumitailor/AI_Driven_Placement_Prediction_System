import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/placement_data.csv")

placed_counts = df["Placed"].value_counts()

plt.figure(figsize=(6,4))
placed_counts.plot(kind="bar")
plt.title("Placement Distribution")
plt.xlabel("Placed")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig(
    "screenshots/placement_distribution.png"
)

print("Chart saved")