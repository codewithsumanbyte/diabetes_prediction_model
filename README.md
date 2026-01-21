# 🩺 Diabetes Prediction Model

A Machine Learning–based web application that predicts whether a person is likely to have diabetes based on medical input features. The model is trained using historical health data and deployed using **Flask** for easy interaction through a web interface.

---

## 📌 Project Overview

Diabetes is a chronic disease that requires early detection to prevent severe complications.  
This project uses **Machine Learning** to analyze patient data and predict the likelihood of diabetes, helping in early diagnosis and decision support.

---

## 🚀 Features

- 🧠 Machine Learning–based prediction
- 🌐 Web interface built with Flask
- 📊 Accepts multiple medical parameters as input
- ⚡ Fast and lightweight deployment
- 📦 Pre-trained model saved using Pickle

---

## 🗂️ Project Structure
Diabetes-Prediction/
│
├── templates/
│   └── index.html        # Frontend HTML file
│
├── app.py                # Flask application
├── model.pkl             # Trained ML model
├── requirements.txt      # Required Python libraries
├── .gitignore            # Git ignored files
└── README.md             # Project documentation

---

## 🧪 Input Parameters

The model uses the following medical features:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

---

## 🛠️ Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- HTML / CSS
- Pickle

---

## ⚙️ Installation & Setup

###  Install Dependencies
```bash
pip install -r requirements.txt
📈 Model Details
Algorithm Used: Machine Learning Classification Model
Training Dataset: Diabetes medical dataset
Model File: model.pkl
Serialization Method: Pickle
✅ Prediction Output
Diabetic – High probability of diabetes
Non-Diabetic – Low probability of diabetes
## 🎯 Use Cases

Early diabetes risk prediction
Academic and learning purposes
Healthcare ML demonstrations
Flask-based ML deployment example
🔮 Future Enhancements
Add prediction confidence score
Improve UI/UX design
Deploy on cloud platforms (Heroku / Render)
Add REST API support
Enhance model accuracy
👨‍💻 Author
Suman Banerjee
AI & ML Engineering Student
Magneta Institute of Technology, Kolkata
📜 Disclaimer
This project is intended for educational purposes only
and should not be used for real-world medical diagnosis.