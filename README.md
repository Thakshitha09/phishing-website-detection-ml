#🔐 Phishing Website Detection Using Machine Learning

A full-stack Machine Learning web application that detects phishing websites using URL-based feature analysis.  
The system compares predictions from a Random Forest model and a Deep Learning model and provides real-time analytics through an admin dashboard.

📌 Problem Statement
Traditional phishing detection methods like blacklists and rule-based systems fail to detect newly generated phishing websites.  
This project uses Machine Learning techniques to analyze URL features and classify websites as **Phishing** or **Legitimate** in real time.

🚀 Features
- 🔎 URL-based phishing detection
- 🌲 Random Forest model prediction
- 🧠 Deep Learning (Neural Network) prediction
- 📊 Model comparison dashboard
- 📈 Real-time analytics (Chart.js visualization)
- 🗂 Prediction history tracking (MySQL database)
- 🔐 Admin login system
- 📡 Auto-refreshing dashboard statistics

🧠 How the System Works
1. User enters a URL.
2. The system extracts URL-based features.
3. Features are passed to:
   - Random Forest model
   - Deep Learning model
4. Both models generate:
   - Prediction (Phishing / Legitimate)
   - Confidence score
5. Results are stored in MySQL.
6. Admin dashboard displays:
   - Total predictions
   - Phishing counts
   - Model disagreements
   - Accuracy comparison

🛠 Technologies Used
### Backend
- Python
- Flask
- MySQL
### Machine Learning
- Scikit-learn (Random Forest)
- TensorFlow / Keras (Deep Learning)
- NumPy
- Pickle
### Frontend
- HTML
- CSS
- Chart.js

## 📊 Dashboard Overview

- Total predictions count
- Random Forest phishing count
- Deep Learning phishing count
- Model disagreement analysis
- Bar chart comparison
- Pie chart distribution

## ⚙ Installation & Setup

1. Clone the repository:
   git clone https://github.com/Thakshitha09/phishing-website-detection-ml.git

2. Navigate to project folder:
   cd phishing-website-detection-ml
   
3. reate virtual environment:
   python -m venv venv

4. Activate virtual environment:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the application:
   python app.py

7. Open in browser:
   http://127.0.0.1:5000

## 📈 Future Improvements

- Real-time phishing dataset updates
- Deployment to cloud (Render / AWS)
- Email alert system
- Model explainability (SHAP/LIME)
- REST API integration

## 👩‍💻 Developed By

Sai Thakshitha Vankadhara  
Machine Learning & Web Development Enthusiast
