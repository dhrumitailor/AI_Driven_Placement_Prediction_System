# 🎓 AI Placement Prediction System

## 📌 Overview

The AI Placement Prediction System is a Machine Learning-based web application designed to predict whether a student is likely to get placed based on academic performance, technical skills, and placement preparation metrics.

The project utilizes a Random Forest Classification model trained on student-related attributes such as CGPA, internships, aptitude scores, communication skills, projects, certifications, and placement training status. The trained model is integrated with a Streamlit web application that provides real-time placement predictions and probability analysis.

---

## 🚀 Features

### Machine Learning

* Random Forest Classification Model
* Placement Prediction
* Probability-Based Decision Making
* Model Persistence using Joblib

### Data Processing

* Dataset Generation
* Data Preprocessing
* Feature Engineering
* Train-Test Split

### Visualization

* Placement Distribution Analysis
* Feature Importance Analysis
* Model Performance Evaluation
* Confusion Matrix Visualization

### Interactive Web Application

* Streamlit-Based Dashboard
* Real-Time Predictions
* User-Friendly Interface
* Probability Score Display

---

## 🛠 Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Core Programming      |
| Pandas       | Data Processing       |
| NumPy        | Numerical Computation |
| Scikit-Learn | Machine Learning      |
| Matplotlib   | Data Visualization    |
| Streamlit    | Web Application       |
| Joblib       | Model Serialization   |

---

## 📂 Project Structure

```text
AI_Placement_Prediction_System
│
├── dataset
│   └── placement_data.csv
│
├── models
│   └── placement_model.pkl
│
├── screenshots
│   ├── placement_distribution.png
│   ├── feature_importance.png
│   └── confusion_matrix.png
│
├── src
│   ├── generate_dataset.py
│   ├── train.py
│   ├── predict.py
│   ├── visualize.py
│   ├── feature_importance.py
│   └── evaluate.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Features

The model uses the following student attributes:

| Feature            | Description                 |
| ------------------ | --------------------------- |
| CGPA               | Academic Performance        |
| Internships        | Number of Internships       |
| AptitudeScore      | Aptitude Test Score         |
| CommunicationScore | Communication Skills Score  |
| Projects           | Number of Projects          |
| Certifications     | Professional Certifications |
| PlacementTraining  | Placement Training Status   |

### Target Variable

```text
Placed
0 = Not Placed
1 = Placed
```

---

## 🤖 Machine Learning Pipeline

### Step 1: Dataset Generation

```bash
python src/generate_dataset.py
```

### Step 2: Model Training

```bash
python src/train.py
```

### Step 3: Evaluation

```bash
python src/evaluate.py
```

### Step 4: Feature Importance Analysis

```bash
python src/feature_importance.py
```

---

## 🎯 Model Performance

| Metric       | Value                    |
| ------------ | ------------------------ |
| Algorithm    | Random Forest Classifier |
| Dataset Size | 300 Records              |
| Test Size    | 20%                      |
| Accuracy     | 93.3%                    |

---

## 🌐 Running the Web Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Application

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📷 Screenshots

### Placement Prediction Dashboard

Add screenshot here:

```text
screenshots/dashboard.png
```

### Placement Distribution

Add screenshot here:

```text
screenshots/placement_distribution.png
```

### Feature Importance

Add screenshot here:

```text
screenshots/feature_importance.png
```

### Confusion Matrix

Add screenshot here:

```text
screenshots/confusion_matrix.png
```

---

## 🔍 Key Concepts Demonstrated

* Machine Learning Classification
* Random Forest Algorithm
* Feature Importance Analysis
* Data Visualization
* Model Evaluation
* Streamlit Development
* Predictive Analytics
* End-to-End ML Pipeline

---

## 🎓 Learning Outcomes

Through this project, the following concepts were implemented and understood:

* Data Collection & Preparation
* Model Training & Evaluation
* Feature Analysis
* Classification Techniques
* Web App Integration
* Machine Learning Deployment

---

## 🔮 Future Enhancements

* Real Student Dataset Integration
* Resume Analysis Module
* Skill Gap Assessment
* Placement Recommendation Engine
* Deep Learning Models
* Cloud Deployment
* Recruiter Dashboard
* Student Performance Tracking

---

## 👨‍💻 Author

Dhrumi

## 📜 License

This project is developed for educational and learning purposes.
