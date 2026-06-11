# import streamlit as st
# import pandas as pd
# import joblib

# model = joblib.load("models/placement_model.pkl")

# st.set_page_config(
#     page_title="AI Placement Predictor",
#     page_icon="🎓"
# )

# st.title("🎓 AI Placement Prediction System")

# st.write(
#     "Predict whether a student is likely to get placed based on academic and skill parameters."
# )

# cgpa = st.slider("CGPA", 5.0, 10.0, 7.5)

# internships = st.number_input(
#     "Internships",
#     min_value=0,
#     max_value=5,
#     value=1
# )

# aptitude = st.slider(
#     "Aptitude Score",
#     40,
#     100,
#     70
# )

# communication = st.slider(
#     "Communication Score",
#     40,
#     100,
#     70
# )

# projects = st.number_input(
#     "Projects",
#     min_value=0,
#     max_value=10,
#     value=2
# )

# certifications = st.number_input(
#     "Certifications",
#     min_value=0,
#     max_value=10,
#     value=1
# )

# training = st.selectbox(
#     "Placement Training",
#     [0, 1]
# )

# if st.button("Predict"):

#     student = pd.DataFrame({
#         "CGPA":[cgpa],
#         "Internships":[internships],
#         "AptitudeScore":[aptitude],
#         "CommunicationScore":[communication],
#         "Projects":[projects],
#         "Certifications":[certifications],
#         "PlacementTraining":[training]
#     })

#     prediction = model.predict(student)


#     probability = model.predict_proba(student)

# placement_probability = probability[0][1] * 100

# st.write(
#     f"Placement Probability: {placement_probability:.2f}%"
# )

    
# if prediction[0] == 1:
#         st.success("Likely to be Placed ✅")
# else:
#         st.error("Placement Risk ⚠️")


# st.image(
#     "screenshots/feature_importance.png",
#     caption="Feature Importance"
# )

import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/placement_model.pkl")

# Page settings
st.set_page_config(
    page_title="AI Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 AI Placement Prediction System")

st.write(
    "Predict whether a student is likely to get placed based on academic and skill parameters."
)

# Inputs
cgpa = st.slider(
    "CGPA",
    5.0,
    10.0,
    7.5
)

internships = st.number_input(
    "Internships",
    min_value=0,
    max_value=5,
    value=1
)

aptitude = st.slider(
    "Aptitude Score",
    40,
    100,
    70
)

communication = st.slider(
    "Communication Score",
    40,
    100,
    70
)

projects = st.number_input(
    "Projects",
    min_value=0,
    max_value=10,
    value=2
)

certifications = st.number_input(
    "Certifications",
    min_value=0,
    max_value=10,
    value=1
)

training = st.selectbox(
    "Placement Training",
    [0, 1]
)

# Prediction
if st.button("Predict"):

    student = pd.DataFrame({
        "CGPA": [cgpa],
        "Internships": [internships],
        "AptitudeScore": [aptitude],
        "CommunicationScore": [communication],
        "Projects": [projects],
        "Certifications": [certifications],
        "PlacementTraining": [training]
    })

    prediction = model.predict(student)

    probability = model.predict_proba(student)

    placement_probability = probability[0][1] * 100

    st.metric(
        label="Placement Probability",
        value=f"{placement_probability:.2f}%"
    )

    if prediction[0] == 1:
        st.success("Likely to be Placed ✅")
    else:
        st.error("Placement Risk ⚠️")

# Feature Importance Chart
st.subheader("📊 Feature Importance")

st.image(
    "screenshots/feature_importance.png",
    caption="Feature Importance Analysis",
    use_container_width=True
)

