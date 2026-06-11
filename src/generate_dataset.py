import pandas as pd
import numpy as np

np.random.seed(42)

rows = []

for _ in range(300):

    cgpa = round(np.random.uniform(5.0, 10.0), 2)

    internships = np.random.randint(0, 4)

    aptitude = np.random.randint(40, 100)

    communication = np.random.randint(40, 100)

    projects = np.random.randint(0, 6)

    certifications = np.random.randint(0, 5)

    training = np.random.randint(0, 2)

    score = (
        cgpa * 10
        + internships * 5
        + aptitude * 0.3
        + communication * 0.2
        + projects * 3
        + certifications * 2
        + training * 10
    )

    placed = 1 if score > 100 else 0

    rows.append([
        cgpa,
        internships,
        aptitude,
        communication,
        projects,
        certifications,
        training,
        placed
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "CGPA",
        "Internships",
        "AptitudeScore",
        "CommunicationScore",
        "Projects",
        "Certifications",
        "PlacementTraining",
        "Placed"
    ]
)

df.to_csv(
    "dataset/placement_data.csv",
    index=False
)

print("Dataset generated:", len(df))