import joblib
import pandas as pd

model = joblib.load(
    "../models/placement_model.pkl"
)

student = pd.DataFrame({
    "CGPA":[8.4],
    "Internships":[2],
    "AptitudeScore":[85],
    "CommunicationScore":[80],
    "Projects":[3],
    "Certifications":[2],
    "PlacementTraining":[1]
})

prediction = model.predict(student)

if prediction[0] == 1:
    print("Placed")
else:
    print("Not Placed")